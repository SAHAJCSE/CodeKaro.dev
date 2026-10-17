# Save Bandwidth Using Compression

*Source: Practice-Test 6*

Compress a text message: each **consecutive run** of a character longer than 1 becomes `char + count`.

`static String compressMsg(String textMsg)` in `class Result`

`ggkkgdddgggg` -> `g2k2gd3g4`, `abddddddd` -> `abd7`

Edit `Solution.java`, then run:  `python3 judge.py save-bandwidth-compression`
