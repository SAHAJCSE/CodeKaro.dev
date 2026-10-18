# Valid email address

*Source: Practice-Test 11*

Validate an email. It is **valid** only if it has exactly one `@`, exactly one `.`, the `.` comes **after** the `@`, and there is at least one character between `@` and `.`.
Throw the user-defined `EmailException` for an invalid address, **catch it inside** `isValidEmail`, and print `1` (valid) or `0` (invalid).

`static void isValidEmail(String email)` in `class Main`

`abc@gmail.com` -> 1, `email@codequotient` -> 0, `user.name@domain` -> 0, `student@college.edu` -> 1

Edit `Solution.java`, then run:  `python3 judge.py valid-email-address`
