# College Seats Are Reserved

*Source: Practice-Test 14*

`A[i]` is the age for which seat `i` is reserved, `B[i]` the age of applicant `i`. Return `true` if **every seat can be filled** (both arrays contain the same ages with the same frequencies, in any order).

`static boolean allSeatsFilled(int[] A, int[] B)` in `class Result`

`[11,12,13,12,13]` / `[12,13,11,12,13]` -> YES, `[11,12,13]` / `[12,13,12]` -> NO

Constraints: `1 <= N <= 10^5`, `1 <= A[i], B[i] <= 100`

Edit `Solution.java`, then run:  `python3 judge.py college-seats-reserved`
