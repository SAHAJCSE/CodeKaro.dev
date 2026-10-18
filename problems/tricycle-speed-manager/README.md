# Tricycle Speed Manager

*Source: Practice-Test 9*

`class Tricycle` with `private int speed`.

| Member | Behaviour |
|---|---|
| `Tricycle()` | speed = 5 |
| `Tricycle(Tricycle t)` | copy of `t`'s speed (independent object) |
| `void setSpeed(int s)` / `int getSpeed()` | set / get |
| `void incr()` / `void brake()` | speed +1 / -1 |

Driver: t1 default, incr; t2 = copy of t1, incr, setSpeed(x); brake both.

Edit `Solution.java`, then run:  `python3 judge.py tricycle-speed-manager`
