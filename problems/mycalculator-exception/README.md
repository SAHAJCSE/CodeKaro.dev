# MyCalculator Exception

*Source: Practice-Test 12*

`class MyException extends Exception` (with an `int code`) is provided. Implement `static void power(int n, int p)` in `class Main` that **throws, catches (inside `power`) and prints the error code**:

1. if `n` or `p` is negative -> throw `MyException(-1)` -> print `-1`
2. else if both are `0` -> throw `MyException(-2)` -> print `-2`
3. otherwise print `n^p`

Input `2 3` `-3 2` `0 0` `5 0` `0 5` -> `8 -1 -2 1 0` (one per line)

Edit `Solution.java`, then run:  `python3 judge.py mycalculator-exception`
