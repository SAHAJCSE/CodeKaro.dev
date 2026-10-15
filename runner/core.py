"""Core execution engine for compiling and running Java OOP solutions."""
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
import uuid
from pathlib import Path

# Base paths
ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
COMMON = ROOT / "common"

try:
    from runner.scanner import scan_untrusted_code
except ImportError:
    from scanner import scan_untrusted_code

PROBLEM_ID = re.compile(r"^[a-z0-9-]+$")
MAX_REQUEST_BYTES = 100 * 1024  # 100 KB max HTTP request payload
MAX_CODE_BYTES = 20 * 1024      # 20 KB max code size
MAX_OUTPUT_BYTES = 64 * 1024    # 64 KB max captured output

JAVAC_TIMEOUT_SECONDS = int(os.environ.get("JAVAC_TIMEOUT_SECONDS", "30"))
JAVA_TIMEOUT_SECONDS = int(os.environ.get("JAVA_TIMEOUT_SECONDS", "10"))


def get_problem_ids():
    """Return sorted list of available problem IDs."""
    if not PROBLEMS.is_dir():
        return []
    return sorted(path.name for path in PROBLEMS.iterdir() if path.is_dir())


def is_valid_problem(problem_id: str) -> bool:
    """Check if problem_id matches expected format and exists on disk."""
    if not isinstance(problem_id, str) or not PROBLEM_ID.fullmatch(problem_id):
        return False
    return (PROBLEMS / problem_id).is_dir()


def get_problem_total_tests(problem_id: str) -> int:
    """Extract the expected total number of test assertions from Test.java."""
    test_path = PROBLEMS / problem_id / "Test.java"
    if not test_path.is_file():
        return 0
    try:
        content = test_path.read_text(encoding="utf-8")
        matches = re.findall(r"Judge\.(?:eq|out|io)\s*\(", content)
        return len(matches)
    except Exception:
        return 0


def normalize_and_escape_text(s: str | None) -> str | None:
    """
    1. Normalize line endings: replace \\r\\n and \\r with \\n.
    2. Make control characters visible: \\0 for NUL, \\xNN for non-printable chars.
       Preserves standard \\n and \\t.
    """
    if s is None:
        return None
    # Normalize line endings
    text = s.replace("\r\n", "\n").replace("\r", "\n")
    # Make control characters visible
    out = []
    for ch in text:
        code = ord(ch)
        if ch == "\0":
            out.append("\\0")
        elif ch in ("\n", "\t"):
            out.append(ch)
        elif code < 32 or (127 <= code <= 159):
            out.append(f"\\x{code:02x}")
        else:
            out.append(ch)
    return "".join(out)


def run_solution(problem_id: str, source: str, mode: str = "run") -> dict:
    """
    Compile and test a user solution in an isolated temporary directory.

    Supported modes:
      - "run": executes tests but only returns sample tests (sample == True).
               status, passedTests and totalTests are computed solely from sample tests.
               Hidden test names and expected/actual are never leaked.
      - "submit": executes tests and evaluates against all tests.
               Returns full details ONLY for the first failing test.
               For all other tests sends only { index, passed, status } with no hidden test names.

    Returns structured JSON:
        {
            "status": "ACCEPTED" | "WRONG_ANSWER" | "COMPILE_ERROR" | "RUNTIME_ERROR" | "TIME_LIMIT_EXCEEDED",
            "passed": bool,
            "exitCode": int | None,
            "compileError": str | None,
            "mode": "run" | "submit",
            "totalTests": int,
            "passedTests": int,
            "firstFailedIndex": int | None,
            "stoppedEarly": bool,
            "stoppedAtTest": int | None,
            "testsNotRun": int,
            "runtimeMs": int,
            "testCases": list[dict],
            "output": str,
            "saved": True
        }
    """
    if not is_valid_problem(problem_id):
        raise ValueError(f"Unknown or invalid problem: '{problem_id}'")

    mode = mode.lower().strip() if isinstance(mode, str) else "run"
    if mode not in ("run", "submit"):
        raise ValueError("Mode must be either 'run' or 'submit'.")

    problem_dir = PROBLEMS / problem_id
    test_src = problem_dir / "Test.java"
    judge_src = COMMON / "Judge.java"

    if not test_src.is_file():
        raise FileNotFoundError(f"Missing Test.java for problem: '{problem_id}'")
    if not judge_src.is_file():
        raise FileNotFoundError("Missing common/Judge.java test harness")

    expected_total_tests = get_problem_total_tests(problem_id)

    # Security check: 20KB max code size limit
    if len(source.encode("utf-8")) > MAX_CODE_BYTES:
        return {
            "status": "COMPILE_ERROR",
            "passed": False,
            "exitCode": None,
            "compileError": "Code size exceeds maximum limit of 20KB.",
            "mode": mode,
            "totalTests": 0,
            "passedTests": 0,
            "firstFailedIndex": None,
            "stoppedEarly": False,
            "stoppedAtTest": None,
            "testsNotRun": expected_total_tests,
            "runtimeMs": 0,
            "testCases": [],
            "output": f"=== {problem_id} ===\n[COMPILATION ERROR]\nCode size exceeds maximum limit of 20KB.",
            "saved": True,
        }

    # Security check: static scan for untrusted / sandbox escape APIs
    is_safe, scan_err = scan_untrusted_code(source)
    if not is_safe:
        return {
            "status": "COMPILE_ERROR",
            "passed": False,
            "exitCode": None,
            "compileError": scan_err,
            "mode": mode,
            "totalTests": 0,
            "passedTests": 0,
            "firstFailedIndex": None,
            "stoppedEarly": False,
            "stoppedAtTest": None,
            "testsNotRun": expected_total_tests,
            "runtimeMs": 0,
            "testCases": [],
            "output": f"=== {problem_id} ===\n[COMPILATION ERROR]\n{scan_err}",
            "saved": True,
        }

    with tempfile.TemporaryDirectory(prefix=f"judge_{problem_id}_") as tmp_dir:
        tmp = Path(tmp_dir)

        # Write submitted solution and copy test harness files
        (tmp / "Solution.java").write_text(source, encoding="utf-8")
        shutil.copy(test_src, tmp / "Test.java")

        # Reuse precompiled Judge class files if available to speed up compilation
        judge_classes = list(judge_src.parent.glob("Judge*.class"))
        if judge_classes:
            for jc in judge_classes:
                shutil.copy(jc, tmp / jc.name)
        else:
            shutil.copy(judge_src, tmp / "Judge.java")

        java_files = [str(f) for f in tmp.glob("*.java")]

        # Step 1: Compilation with javac (speed-optimized for container environments)
        javac_cmd = [
            "javac",
            "-J-XX:TieredStopAtLevel=1",
            "-J-Xmx128m",
            "-cp",
            str(tmp),
            "-d",
            str(tmp),
        ] + java_files

        try:
            compile_res = subprocess.run(
                javac_cmd,
                capture_output=True,
                text=True,
                timeout=JAVAC_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            return {
                "status": "COMPILE_ERROR",
                "passed": False,
                "exitCode": None,
                "compileError": f"Compilation timed out after {JAVAC_TIMEOUT_SECONDS}s.",
                "mode": mode,
                "totalTests": 0,
                "passedTests": 0,
                "firstFailedIndex": None,
                "stoppedEarly": False,
                "stoppedAtTest": None,
                "testsNotRun": expected_total_tests,
                "runtimeMs": JAVAC_TIMEOUT_SECONDS * 1000,
                "testCases": [],
                "output": f"=== {problem_id} ===\n[COMPILATION ERROR]\nCompilation timed out after {JAVAC_TIMEOUT_SECONDS}s.",
                "saved": True,
            }

        if compile_res.returncode != 0:
            err = compile_res.stderr.replace(str(tmp) + os.sep, "").replace(str(tmp), "").strip()
            err = normalize_and_escape_text(err)
            return {
                "status": "COMPILE_ERROR",
                "passed": False,
                "exitCode": compile_res.returncode,
                "compileError": err,
                "mode": mode,
                "totalTests": 0,
                "passedTests": 0,
                "firstFailedIndex": None,
                "stoppedEarly": False,
                "stoppedAtTest": None,
                "testsNotRun": expected_total_tests,
                "runtimeMs": 0,
                "testCases": [],
                "output": f"=== {problem_id} ===\n[COMPILATION ERROR]\n{err}".strip(),
                "saved": True,
            }

        # Remove .java source files so user code cannot read them from disk
        for jf in tmp.glob("*.java"):
            try:
                jf.unlink()
            except OSError:
                pass

        # Step 2: Execution with java (5s timeout, -Xmx128m, -Xss512k, -XX:ActiveProcessorCount=1)
        # Result marker is passed strictly via stdin, never via system properties or argv
        marker = f"__OJ_RESULT_{uuid.uuid4().hex}__"
        java_cmd = [
            "java",
            "-XX:TieredStopAtLevel=1",
            "-Xmx128m",
            "-Xss512k",
            "-XX:ActiveProcessorCount=1",
            "-cp",
            str(tmp),
            "Test",
        ]

        start_time = time.perf_counter()
        try:
            run_res = subprocess.run(
                java_cmd,
                input=f"{marker}\n",
                capture_output=True,
                text=True,
                timeout=JAVA_TIMEOUT_SECONDS,
                cwd=str(tmp),
            )
            runtime_ms = round((time.perf_counter() - start_time) * 1000)
            timed_out = False
        except subprocess.TimeoutExpired:
            runtime_ms = round((time.perf_counter() - start_time) * 1000)
            timed_out = True
            run_res = None

        if timed_out:
            return {
                "status": "TIME_LIMIT_EXCEEDED",
                "passed": False,
                "exitCode": None,
                "compileError": None,
                "mode": mode,
                "totalTests": 0,
                "passedTests": 0,
                "firstFailedIndex": 0,
                "stoppedEarly": True,
                "stoppedAtTest": 0,
                "testsNotRun": expected_total_tests,
                "runtimeMs": max(runtime_ms, JAVA_TIMEOUT_SECONDS * 1000),
                "testCases": [],
                "output": f"Time Limit Exceeded: Execution took longer than {JAVA_TIMEOUT_SECONDS} seconds.",
                "saved": True,
            }

        # Step 3: Parse stdout lines, extract marker JSON line
        raw_test_cases = []
        json_data = None
        cleaned_lines = []

        stdout_text = run_res.stdout or ""
        # Search for marker line across entire output first so JSON results are never dropped
        for line in stdout_text.splitlines():
            if line.startswith(marker):
                raw_json = line[len(marker):].strip()
                try:
                    json_data = json.loads(raw_json)
                except Exception:
                    pass
            else:
                cleaned_lines.append(line)

        raw_human_output = "\n".join(cleaned_lines)
        if run_res.stderr:
            raw_human_output = f"{raw_human_output}\n{run_res.stderr}" if raw_human_output else run_res.stderr
        raw_human_output = raw_human_output.strip()
        if len(raw_human_output) > MAX_OUTPUT_BYTES:
            raw_human_output = raw_human_output[:MAX_OUTPUT_BYTES] + "\n[output truncated]"

        if json_data and isinstance(json_data, dict) and "tests" in json_data:
            raw_test_cases = json_data.get("tests", [])

        # Normalize test case strings (line endings and control characters)
        for t in raw_test_cases:
            t["stdout"] = normalize_and_escape_text(t.get("stdout"))
            t["expected"] = normalize_and_escape_text(t.get("expected"))
            t["actual"] = normalize_and_escape_text(t.get("actual"))

        # Step 4: Detect whether execution stopped early (e.g. TLE halted JVM)
        any_tle = any(t.get("status") == "TIME_LIMIT_EXCEEDED" for t in raw_test_cases)
        any_runtime_err = any(t.get("status") == "RUNTIME_ERROR" for t in raw_test_cases)

        stopped_early = bool(any_tle or (run_res.returncode != 0 and len(raw_test_cases) < expected_total_tests))
        tests_not_run = max(0, expected_total_tests - len(raw_test_cases)) if stopped_early else 0
        stopped_at_test = len(raw_test_cases) if stopped_early else None

        # Step 5: Process testCases & compute status according to mode
        title_line = next((l for l in raw_human_output.splitlines() if l.startswith("===")), f"=== {problem_id} ===")

        if mode == "run":
            # Filter to sample tests only
            sample_tests = [t for t in raw_test_cases if t.get("sample")]
            total_tests = len(sample_tests)
            passed_tests = sum(1 for t in sample_tests if t.get("passed"))

            # Determine status from sample tests only
            sample_tle = any(t.get("status") == "TIME_LIMIT_EXCEEDED" for t in sample_tests)
            sample_runtime_err = any(t.get("status") == "RUNTIME_ERROR" for t in sample_tests)

            if sample_tle:
                status = "TIME_LIMIT_EXCEEDED"
            elif sample_runtime_err or "Exception in thread" in raw_human_output or "OutOfMemoryError" in raw_human_output or "StackOverflowError" in raw_human_output or (run_res.returncode != 0 and total_tests == 0):
                status = "RUNTIME_ERROR"
            elif total_tests > 0 and passed_tests == total_tests:
                status = "ACCEPTED"
            else:
                status = "WRONG_ANSWER"

            passed = (status == "ACCEPTED")

            # First failed index among sample tests
            first_failed_index = None
            for t in sample_tests:
                if not t.get("passed"):
                    first_failed_index = t.get("index")
                    break

            # Filtered test cases for response
            response_test_cases = sample_tests

            # Build sanitized output containing ONLY sample tests (no hidden tests leaked)
            out_lines = [title_line]
            for t in sample_tests:
                if t.get("passed"):
                    out_lines.append(f"[PASS] {t.get('name')}")
                else:
                    out_lines.append(f"[FAIL] {t.get('name')}")
                    if t.get("status") == "TIME_LIMIT_EXCEEDED":
                        out_lines.append("       Time Limit Exceeded (> 2000 ms)")
                    elif t.get("actual") and "Runtime Error:" in t["actual"]:
                        out_lines.append(f"       {t['actual']}")
                    else:
                        if t.get("expected") is not None:
                            out_lines.append(f"       Expected: {t['expected']}")
                        if t.get("actual") is not None:
                            out_lines.append(f"       Actual  : {t['actual']}")

            out_lines.append("-----------------------------------------")
            verdict_str = "ACCEPTED" if status == "ACCEPTED" else ("TIME LIMIT EXCEEDED" if status == "TIME_LIMIT_EXCEEDED" else "WRONG ANSWER")
            out_lines.append(f"Result: {passed_tests}/{total_tests} passed  ->  {verdict_str}")
            final_output = "\n".join(out_lines)

        else:
            # Mode: "submit" - uses ALL tests
            total_tests = len(raw_test_cases)
            passed_tests = sum(1 for t in raw_test_cases if t.get("passed"))

            if any_tle or "TIME LIMIT EXCEEDED" in raw_human_output or "Time Limit Exceeded" in raw_human_output:
                status = "TIME_LIMIT_EXCEEDED"
            elif any_runtime_err or "Exception in thread" in raw_human_output or "OutOfMemoryError" in raw_human_output or "StackOverflowError" in raw_human_output or (run_res.returncode != 0 and total_tests == 0):
                status = "RUNTIME_ERROR"
            elif total_tests > 0 and passed_tests == total_tests and run_res.returncode == 0:
                status = "ACCEPTED"
            else:
                status = "WRONG_ANSWER"

            passed = (status == "ACCEPTED")

            # Find first failing test index
            first_failed_index = None
            for t in raw_test_cases:
                if not t.get("passed"):
                    first_failed_index = t.get("index")
                    break

            # In submit mode:
            # Full details ONLY for the first failing test.
            # All other tests send only { index, passed, status } with no names of hidden tests.
            response_test_cases = []
            for t in raw_test_cases:
                idx = t.get("index")
                if idx == first_failed_index:
                    # First failing test: full details
                    failed_record = {
                        "index": idx,
                        "passed": False,
                        "status": t.get("status", "FAILED"),
                        "expected": t.get("expected"),
                        "actual": t.get("actual"),
                        "stdout": t.get("stdout", ""),
                        "runtimeMs": t.get("runtimeMs", 0),
                        "sample": t.get("sample", False),
                    }
                    if t.get("sample"):
                        failed_record["name"] = t.get("name")
                    else:
                        failed_record["name"] = f"Hidden Test #{idx + 1}"
                    response_test_cases.append(failed_record)
                else:
                    # Passed test or subsequent failing test: minimal info
                    response_test_cases.append({
                        "index": idx,
                        "passed": t.get("passed", False),
                        "status": t.get("status", "PASSED" if t.get("passed") else "FAILED"),
                    })

            # Submit mode output: summary without leaking hidden test names
            out_lines = [title_line]
            out_lines.append("-----------------------------------------")
            verdict_str = "ACCEPTED" if status == "ACCEPTED" else ("TIME LIMIT EXCEEDED" if status == "TIME_LIMIT_EXCEEDED" else "WRONG ANSWER")
            out_lines.append(f"Result: {passed_tests}/{total_tests} passed  ->  {verdict_str}")
            if first_failed_index is not None and first_failed_index < len(raw_test_cases):
                failed_t = raw_test_cases[first_failed_index]
                test_label = failed_t.get("name") if failed_t.get("sample") else f"Hidden Test #{first_failed_index + 1}"
                out_lines.append(f"\nFailed on {test_label}:")
                if failed_t.get("expected") is not None:
                    out_lines.append(f"  Expected: {failed_t['expected']}")
                if failed_t.get("actual") is not None:
                    out_lines.append(f"  Actual  : {failed_t['actual']}")
            final_output = "\n".join(out_lines)

        return {
            "status": status,
            "passed": passed,
            "exitCode": run_res.returncode,
            "compileError": None,
            "mode": mode,
            "totalTests": total_tests,
            "passedTests": passed_tests,
            "firstFailedIndex": first_failed_index,
            "stoppedEarly": stopped_early,
            "stoppedAtTest": stopped_at_test,
            "testsNotRun": tests_not_run,
            "runtimeMs": runtime_ms,
            "testCases": response_test_cases,
            "output": final_output,
            "saved": True,
        }
