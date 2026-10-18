#!/usr/bin/env python3
"""Code-Karo.dev judge runner.   python3 judge.py list | <problem-id> [--ref] | all [--ref]"""
import os, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
PROBLEMS = os.path.join(ROOT, "problems")
REFERENCE = os.path.join(ROOT, "reference")

def ids():
    return sorted(d for d in os.listdir(PROBLEMS) if os.path.isdir(os.path.join(PROBLEMS, d)))

def run(pid, ref):
    pdir = os.path.join(PROBLEMS, pid)
    if not os.path.isdir(pdir):
        print(f"Unknown problem '{pid}'. Try: python3 judge.py list"); return False
    tmp = tempfile.mkdtemp(prefix="judge_")
    try:
        src = os.path.join(REFERENCE, pid, "Solution.java") if ref else os.path.join(pdir, "Solution.java")
        shutil.copy(src, os.path.join(tmp, "Solution.java"))
        shutil.copy(os.path.join(pdir, "Test.java"), tmp)
        shutil.copy(os.path.join(ROOT, "common", "Judge.java"), tmp)
        c = subprocess.run(["javac", "-d", tmp] + [os.path.join(tmp, f) for f in os.listdir(tmp) if f.endswith(".java")],
                           capture_output=True, text=True)
        if c.returncode != 0:
            print(f"\n=== {pid} ===\n[COMPILATION ERROR]\n{c.stderr.replace(tmp + os.sep, '')}"); return False
        r = subprocess.run(["java", "-cp", tmp, "Test"], text=True, input="")
        return r.returncode == 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

def main():
    a = [x for x in sys.argv[1:] if x != "--ref"]; ref = "--ref" in sys.argv
    if not a or a[0] in ("-h", "--help"): print(__doc__); return
    if a[0] == "list":
        for p in ids(): print(p)
        return
    targets = ids() if a[0] == "all" else a
    results = {p: run(p, ref) for p in targets}
    if len(targets) > 1:
        print("\n==================== SUMMARY ====================")
        for p, ok in results.items(): print(("PASS  " if ok else "FAIL  ") + p)
        print(f"{sum(results.values())}/{len(results)} problems accepted")
    sys.exit(0 if all(results.values()) else 1)

if __name__ == "__main__":
    main()
