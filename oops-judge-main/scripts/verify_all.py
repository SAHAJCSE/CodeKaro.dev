#!/usr/bin/env python3
"""
Comprehensive verification test script for Code-Karo.dev Runner.

Sends for every problem:
  1. The reference solution (reference/<id>/Solution.java) in submit mode (expects ACCEPTED).
  2. The starter template (problems/<id>/Solution.java) in submit mode (expects WRONG_ANSWER, COMPILE_ERROR, or RUNTIME_ERROR).

Accepts target runner URL as first argument (defaults to http://localhost:8000).
Usage:
  python scripts/verify_all.py
  python scripts/verify_all.py http://localhost:8000
  python scripts/verify_all.py https://oops-judge-runner.onrender.com
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
REFERENCE_DIR = ROOT / "reference"

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "judge_verify_secret")


def post_submit(base_url: str, problem_id: str, code: str) -> dict:
    url = f"{base_url.rstrip('/')}/problems/{problem_id}/run"
    data = json.dumps({"code": code, "mode": "submit"}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "X-Verify-Token": VERIFY_TOKEN,
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=35) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        try:
            return json.loads(err.read().decode("utf-8"))
        except Exception:
            return {"status": f"HTTP_{err.code}", "error": str(err)}
    except Exception as exc:
        return {"status": "NETWORK_ERROR", "error": str(exc)}


def main():
    target_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    target_url = target_url.rstrip("/")

    print("=" * 88)
    print(f"CODE-KARO.DEV COMPREHENSIVE VERIFICATION SUITE")
    print(f"Target Runner: {target_url}")
    print("=" * 88)

    # Health check
    try:
        with urllib.request.urlopen(f"{target_url}/health", timeout=10) as resp:
            health_body = json.loads(resp.read().decode("utf-8"))
            print(f"Health check: OK (status code {resp.status}, payload: {health_body})")
    except Exception as exc:
        print(f"WARNING: Health check failed on {target_url}/health: {exc}")
        print("Make sure the runner is running or wait for cold-start wake-up.")
        sys.exit(1)

    problem_ids = sorted(p.name for p in PROBLEMS_DIR.iterdir() if p.is_dir())
    total_problems = len(problem_ids)
    print(f"Discovered {total_problems} problems to verify.\n")

    # Table Header
    print(f"{'#':>2} | {'Problem ID':<30} | {'Reference':<14} | {'Starter Template':<16} | {'Verdict'}")
    print("-" * 88)

    ref_passes = 0
    starter_passes = 0
    overall_all_passed = True
    start_time = time.perf_counter()

    for idx, pid in enumerate(problem_ids, 1):
        ref_file = REFERENCE_DIR / pid / "Solution.java"
        starter_file = PROBLEMS_DIR / pid / "Solution.java"

        if not ref_file.is_file():
            print(f"{idx:>2} | {pid:<30} | MISSING REF    | -                | FAIL")
            overall_all_passed = False
            continue

        if not starter_file.is_file():
            print(f"{idx:>2} | {pid:<30} | -              | MISSING STARTER  | FAIL")
            overall_all_passed = False
            continue

        ref_code = ref_file.read_text(encoding="utf-8")
        starter_code = starter_file.read_text(encoding="utf-8")

        # 1. Test reference solution (expect ACCEPTED)
        t_ref_start = time.perf_counter()
        ref_res = post_submit(target_url, pid, ref_code)
        ref_time = round((time.perf_counter() - t_ref_start) * 1000)
        ref_status = ref_res.get("status", "UNKNOWN")
        ref_ok = (ref_status == "ACCEPTED")
        if ref_ok:
            ref_passes += 1
            ref_str = f"AC ({ref_time}ms)"
        else:
            ref_str = f"{ref_status[:8]} ({ref_time}ms)"

        # 2. Test starter template (expect WRONG_ANSWER, COMPILE_ERROR, or RUNTIME_ERROR, NOT ACCEPTED)
        t_star_start = time.perf_counter()
        starter_res = post_submit(target_url, pid, starter_code)
        starter_time = round((time.perf_counter() - t_star_start) * 1000)
        starter_status = starter_res.get("status", "UNKNOWN")
        starter_ok = (starter_status in ("WRONG_ANSWER", "COMPILE_ERROR", "RUNTIME_ERROR"))
        if starter_ok:
            starter_passes += 1
            starter_str = f"{starter_status[:9]} ({starter_time}ms)"
        else:
            starter_str = f"{starter_status[:9]} ({starter_time}ms)"

        row_ok = ref_ok and starter_ok
        if not row_ok:
            overall_all_passed = False

        verdict = "PASS" if row_ok else "FAIL"
        print(f"{idx:>2} | {pid:<30} | {ref_str:<14} | {starter_str:<16} | {verdict}")

    elapsed = round(time.perf_counter() - start_time, 2)
    print("-" * 88)
    print(f"\nRESULTS SUMMARY:")
    print(f"  Reference solutions passed (ACCEPTED)          : {ref_passes}/{total_problems}")
    print(f"  Starter templates properly rejected (WA/CE/RE) : {starter_passes}/{total_problems}")
    print(f"  Total verification elapsed time                : {elapsed}s")

    if overall_all_passed and ref_passes == total_problems and starter_passes == total_problems:
        print("\nOVERALL VERDICT: ALL CHECKS PASSED [SUCCESS]")
        sys.exit(0)
    else:
        print("\nOVERALL VERDICT: ONE OR MORE CHECKS FAILED [FAILURE]")
        sys.exit(1)


if __name__ == "__main__":
    main()
