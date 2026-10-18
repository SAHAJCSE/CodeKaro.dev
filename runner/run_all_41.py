#!/usr/bin/env python3
"""Run all 41 reference solutions in submit mode and verify 41/41 ACCEPTED."""
import sys
import time
from pathlib import Path
from runner.core import get_problem_ids, run_solution

def main():
    problem_ids = get_problem_ids()
    total = len(problem_ids)
    print(f"Executing {total} reference solutions in SUBMIT mode...\n")

    passed_count = 0
    start_total = time.perf_counter()

    for idx, pid in enumerate(problem_ids, 1):
        sol_path = Path("reference") / pid / "Solution.java"
        if not sol_path.is_file():
            print(f"[{idx:02d}/{total}] {pid:32} -> MISSING Solution.java")
            continue

        source = sol_path.read_text(encoding="utf-8")
        t0 = time.perf_counter()
        result = run_solution(pid, source, mode="submit")
        dur = round((time.perf_counter() - t0) * 1000)

        status = result.get("status")
        total_tests = result.get("totalTests", 0)
        passed_tests = result.get("passedTests", 0)

        if status == "ACCEPTED":
            passed_count += 1
            print(f"[{idx:02d}/{total}] {pid:32} -> ACCEPTED ({passed_tests}/{total_tests} tests, {dur} ms)")
        else:
            print(f"[{idx:02d}/{total}] {pid:32} -> {status} ({passed_tests}/{total_tests} tests, {dur} ms)")
            if result.get("compileError"):
                print(f"       Compile error: {result['compileError'][:100]}")
            if result.get("output"):
                print(f"       Output snippet: {result['output'][:100]}")

    elapsed = round(time.perf_counter() - start_total, 2)
    print("\n" + "=" * 60)
    print(f"SUMMARY: {passed_count}/{total} ACCEPTED (Total time: {elapsed}s)")
    print("=" * 60)

    if passed_count != total:
        sys.exit(1)

if __name__ == "__main__":
    main()
