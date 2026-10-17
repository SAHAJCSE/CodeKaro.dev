# Implement the Date class

*Source: Practice-Test 6*

Implement `class Date` for a **non-leap year** (Feb always has 28 days). The year is not stored.

| Member | Behaviour |
|---|---|
| `private int month, date` | 1-12 and day of month |
| `Date()` | January 1st |
| `Date(int m, int d)` | sets month and day |
| `int daysInMonth()` | days in the current month (31 for Jan, 28 for Feb ...) |
| `int getDay()` / `int getMonth()` | current values |
| `void nextDay()` | +1 day, wraps to 1st of next month, Dec 31 -> Jan 1 |

No `main` needed.

Edit `Solution.java`, then run:  `python3 judge.py date-class`
