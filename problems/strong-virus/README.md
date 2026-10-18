# Strong Virus Detection

*Source: Practice-Test 1*

A DNA sequence (any printable ASCII, may contain spaces) describes a virus. The virus is **strong** if it has an
`x` and a `y` with **exactly three characters between them**. Return `true` if strong, else `false`.

`boolean isStrongVirus(String dna)` in `class Virus` (instance method)

Example: `txma yert` -> x at index 1, y at index 5, between them `m`, `a`, ` ` -> **YES**
`BMuxp ioqytB yxurN` -> **NO**, `xaxoerylm` -> **YES**

Total length of all sequences <= 10^6.

Edit `Solution.java`, then run:  `python3 judge.py strong-virus`
