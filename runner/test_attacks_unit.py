from runner.scanner import scan_untrusted_code

cases = [
    ('Runtime.getRuntime().exec("ls");', False, 'Runtime.getRuntime'),
    ('System.exit(0);', False, 'System.exit'),
    ('System.getProperty("oj.marker");', False, 'System.getProperty'),
    ('new java.io.File("../Test.java");', False, 'java.io.File*'),
    ('new FileInputStream("../Test.java");', False, 'java.io.File*'),
    ('Class.forName("Judge");', False, 'Class.forName'),
    ('field.setAccessible(true);', False, 'setAccessible'),
    ('String s = "System.exit(0)";', True, None),
    ('// System.exit(0);', True, None),
    ('/* System.getProperty("foo"); */', True, None),
]

all_passed = True
for code, should_pass, expected_name in cases:
    ok, err = scan_untrusted_code(code)
    if ok != should_pass or (not should_pass and expected_name not in (err or '')):
        print(f"FAILED: {code} -> got ok={ok}, err={err}")
        all_passed = False
    else:
        print(f"PASSED: {code[:35]:35} -> ok={ok}, err={err}")

if all_passed:
    print("\nALL UNIT ATTACK CHECKS PASSED!")
