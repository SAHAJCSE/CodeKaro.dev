# class - Box

*Source: Practice-Test 10*

Design `class Box` with **private integer** `length`, `breadth`, `height`.

- default constructor -> all 0
- `Box(int length, int breadth, int height)`
- copy constructor `Box(Box b1)`
- `int getLength()`, `int getBreadth()`, `int getHeight()`
- `long CalculateVolume()`

Sample: `3 4 5` -> default `0 0 0 0`, parameterised `3 4 5 60`, copy `3 4 5 60`.
Constraints: `0 <= dimension <= 10^5` (watch the overflow of the volume!)

Edit `Solution.java`, then run:  `python3 judge.py class-box`
