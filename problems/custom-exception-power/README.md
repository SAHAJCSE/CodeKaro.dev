# Calculate positive power of a positive number

*Source: Practice-Test 15*

Write `class CustomException extends Exception` with a private `String msg`, constructor `CustomException(String message)` and an overridden `String getMessage()` returning the stored message.
Then implement `static int power(int num, int exp) throws CustomException` in `class Main`:

1. if `num` or `exp` is negative -> throw `CustomException("Negative numbers not allowed")`
2. else if both are zero -> throw `CustomException("Both can never be zero")`
3. otherwise return `num^exp`

`-4 -5` -> `Negative numbers not allowed`, `2 2` -> `4`

Edit `Solution.java`, then run:  `python3 judge.py custom-exception-power`
