# Library Book Inventory Management

*Source: Practice-Test 15*

Add each newly arrived book id to the inventory **only if it is not already present** (duplicates inside `newBooks` also count). Return the updated `ArrayList`.

`public static ArrayList<Integer> updateInventory(ArrayList<Integer> books, int[] newBooks)` in `class Main`

`101 102 103 104` + `104 105 106 102 107` -> `101 102 103 104 105 106 107`

Edit `Solution.java`, then run:  `python3 judge.py library-book-inventory`
