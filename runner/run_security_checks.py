#!/usr/bin/env python3
"""Automated security verification test suite for Code-Karo.dev Runner."""
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

BASE_URL = "http://localhost:8000"


def post_run(problem_id: str, code: str, mode: str = "run") -> tuple[int, dict]:
    url = f"{BASE_URL}/problems/{problem_id}/run"
    data = json.dumps({"code": code, "mode": mode}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return resp.status, body
    except urllib.error.HTTPError as err:
        body = json.loads(err.read().decode("utf-8"))
        return err.code, body


def run_checks():
    print("=" * 70)
    print("RUNNING AUTOMATED SECURITY & HARDENING VERIFICATION")
    print("=" * 70)

    # 1. Infinite loop -> TLE
    print("\n[CHECK 1] Infinite loop -> TIME_LIMIT_EXCEEDED")
    code_tle = """
class Box {
    Box() { while (true) {} }
    Box(int l, int b, int h) { while (true) {} }
    Box(Box b) { while (true) {} }
    int getLength() { return 0; }
    int getBreadth() { return 0; }
    int getHeight() { return 0; }
    long CalculateVolume() { return 0; }
}
"""
    status_code, resp = post_run("class-box", code_tle, mode="run")
    print(f"HTTP Status: {status_code}")
    print(f"Verdict: {resp.get('status')}")
    print(f"Runtime: {resp.get('runtimeMs')} ms")
    print(f"Stopped early: {resp.get('stoppedEarly')}")
    assert resp.get("status") == "TIME_LIMIT_EXCEEDED", f"Expected TIME_LIMIT_EXCEEDED, got {resp.get('status')}"
    print("-> PASS: Infinite loop halted with TIME_LIMIT_EXCEEDED")

    # 2. System.exit blocked
    print("\n[CHECK 2] System.exit blocked -> COMPILE_ERROR")
    code_exit = """
class Box {
    Box() { System.exit(0); }
    Box(int l, int b, int h) {}
    Box(Box b) {}
    int getLength() { return 0; }
    int getBreadth() { return 0; }
    int getHeight() { return 0; }
    long CalculateVolume() { return 0; }
}
"""
    status_code, resp = post_run("class-box", code_exit, mode="run")
    print(f"HTTP Status: {status_code}")
    print(f"Verdict: {resp.get('status')}")
    print(f"Compile Error: {resp.get('compileError')}")
    assert resp.get("status") == "COMPILE_ERROR", f"Expected COMPILE_ERROR, got {resp.get('status')}"
    assert "System.exit" in resp.get("compileError", ""), "Expected System.exit in compileError"
    print("-> PASS: System.exit blocked at static scan")

    # 3. getProperty marker attempt blocked
    print("\n[CHECK 3] System.getProperty marker attempt blocked -> COMPILE_ERROR")
    code_prop = """
class Box {
    Box() { String m = System.getProperty("oj.marker"); }
    Box(int l, int b, int h) {}
    Box(Box b) {}
    int getLength() { return 0; }
    int getBreadth() { return 0; }
    int getHeight() { return 0; }
    long CalculateVolume() { return 0; }
}
"""
    status_code, resp = post_run("class-box", code_prop, mode="run")
    print(f"HTTP Status: {status_code}")
    print(f"Verdict: {resp.get('status')}")
    print(f"Compile Error: {resp.get('compileError')}")
    assert resp.get("status") == "COMPILE_ERROR", f"Expected COMPILE_ERROR, got {resp.get('status')}"
    assert "System.getProperty" in resp.get("compileError", ""), "Expected System.getProperty in compileError"
    print("-> PASS: System.getProperty blocked at static scan")

    # 4. 5MB output truncated
    print("\n[CHECK 4] 5MB output truncated -> [output truncated]")
    code_5mb = """
class Box {
    Box() {
        for (int i = 0; i < 100000; i++) {
            System.out.println("01234567890123456789012345678901234567890123456789");
        }
    }
    Box(int l, int b, int h) {}
    Box(Box b) {}
    int getLength() { return 0; }
    int getBreadth() { return 0; }
    int getHeight() { return 0; }
    long CalculateVolume() { return 0; }
}
"""
    status_code, resp = post_run("class-box", code_5mb, mode="run")
    print(f"HTTP Status: {status_code}")
    print(f"Verdict: {resp.get('status')}")
    out = resp.get("output", "")
    test_out = resp.get("testCases", [{}])[0].get("stdout", "") if resp.get("testCases") else ""
    truncated_marker_found = ("[output truncated]" in out) or ("[output truncated]" in test_out)
    print(f"Truncated note found: {truncated_marker_found}")
    print(f"Total response output size: {len(out)} bytes")
    assert truncated_marker_found, "Expected '[output truncated]' marker"
    assert len(out) <= 66000, f"Output length {len(out)} exceeded max limit"
    print("-> PASS: 5MB output safely bounded and truncated to 64KB")

    # 5. Deep recursion (StackOverflowError) -> RUNTIME_ERROR
    print("\n[CHECK 5] Deep recursion (StackOverflowError) -> RUNTIME_ERROR")
    code_rec = """
class Box {
    static void recurse() { recurse(); }
    Box() { recurse(); }
    Box(int l, int b, int h) {}
    Box(Box b) {}
    int getLength() { return 0; }
    int getBreadth() { return 0; }
    int getHeight() { return 0; }
    long CalculateVolume() { return 0; }
}
"""
    status_code, resp = post_run("class-box", code_rec, mode="run")
    print(f"HTTP Status: {status_code}")
    print(f"Verdict: {resp.get('status')}")
    print(f"First test error: {resp.get('testCases', [{}])[0].get('actual') if resp.get('testCases') else 'N/A'}")
    assert resp.get("status") == "RUNTIME_ERROR", f"Expected RUNTIME_ERROR, got {resp.get('status')}"
    print("-> PASS: Deep recursion reported as RUNTIME_ERROR")

    # 6. Memory bomb (huge array) -> RUNTIME_ERROR without crashing server
    print("\n[CHECK 6] Memory bomb (huge array) -> RUNTIME_ERROR (server healthy)")
    code_oom = """
class Box {
    Box() {
        long[][] bomb = new long[10000][100000];
    }
    Box(int l, int b, int h) {}
    Box(Box b) {}
    int getLength() { return 0; }
    int getBreadth() { return 0; }
    int getHeight() { return 0; }
    long CalculateVolume() { return 0; }
}
"""
    status_code, resp = post_run("class-box", code_oom, mode="run")
    print(f"HTTP Status: {status_code}")
    print(f"Verdict: {resp.get('status')}")
    assert resp.get("status") == "RUNTIME_ERROR", f"Expected RUNTIME_ERROR, got {resp.get('status')}"
    # Verify server is still alive and answering health checks
    with urllib.request.urlopen(f"{BASE_URL}/health") as h_resp:
        h_body = json.loads(h_resp.read().decode())
        assert h_body.get("status") == "ok", "Server was crashed by memory bomb"
    print("-> PASS: Memory bomb reported as RUNTIME_ERROR, runner remained completely stable")

    # 7. Reading ../ files blocked
    print("\n[CHECK 7] Reading ../ files blocked -> COMPILE_ERROR")
    code_file = """
import java.io.*;
class Box {
    Box() {
        try {
            BufferedReader br = new BufferedReader(new FileReader("../Test.java"));
        } catch (Exception e) {}
    }
    Box(int l, int b, int h) {}
    Box(Box b) {}
    int getLength() { return 0; }
    int getBreadth() { return 0; }
    int getHeight() { return 0; }
    long CalculateVolume() { return 0; }
}
"""
    status_code, resp = post_run("class-box", code_file, mode="run")
    print(f"HTTP Status: {status_code}")
    print(f"Verdict: {resp.get('status')}")
    print(f"Compile Error: {resp.get('compileError')}")
    assert resp.get("status") == "COMPILE_ERROR", f"Expected COMPILE_ERROR, got {resp.get('status')}"
    assert "java.io.File*" in resp.get("compileError", ""), "Expected file API blocked in compileError"
    print("-> PASS: Reading ../ files blocked by static scanner")

    # 8. 30 rapid requests -> 429s appear
    print("\n[CHECK 8] 30 rapid requests -> 429s appear")
    rapid_results = []
    dummy_code = """
class Box {
    private int l, b, h;
    Box() {}
    Box(int l, int b, int h) { this.l = l; this.b = b; this.h = h; }
    Box(Box b1) { this.l = b1.l; this.b = b1.b; this.h = b1.h; }
    int getLength() { return l; }
    int getBreadth() { return b; }
    int getHeight() { return h; }
    long CalculateVolume() { return (long)l * b * h; }
}
"""
    count_429 = 0
    count_200 = 0
    for i in range(30):
        code_status, body = post_run("class-box", dummy_code, mode="run")
        if code_status == 429:
            count_429 += 1
        elif code_status == 200:
            count_200 += 1
        rapid_results.append((i + 1, code_status, body.get("status") or body.get("error")[:30]))

    print(f"Results of 30 rapid requests: {count_200} succeeded (200), {count_429} rate-limited (429)")
    sample_429 = next((res for res in rapid_results if res[1] == 429), None)
    if sample_429:
        print(f"Sample 429 response on request #{sample_429[0]}: {sample_429[2]}...")
    assert count_429 > 0, "Expected 429 rate limit responses among 30 requests"
    print("-> PASS: Rate limiter successfully returned 429s when limit was exceeded")

    print("\n" + "=" * 70)
    print("ALL 8 AUTOMATED HARDENING CHECKS PASSED!")
    print("=" * 70)


if __name__ == "__main__":
    run_checks()
