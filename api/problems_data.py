"""Pre-bundled problem data for Vercel serverless execution."""

PROBLEMS = {
  "airline-ticket-concat": {
    "id": "airline-ticket-concat",
    "title": "The Airline Ticket - Concatenate two strings",
    "summary": "Concatenate two strings **without** `String.concat` / `+`: copy `str1` followed by `str2` into the char array `result` (it is at least `len1 + len2` long).",
    "readme": "# The Airline Ticket - Concatenate two strings\n\n*Source: Practice-Test 10*\n\nConcatenate two strings **without** `String.concat` / `+`: copy `str1` followed by `str2` into the char array `result` (it is at least `len1 + len2` long).\n\n`static void strcat(char[] result, char[] str1, char[] str2)` in `class Main`\n\n`Code` + `Quotient` -> `CodeQuotient`, `John` + `Doe` -> `JohnDoe`\n\nEdit `Solution.java`, then run:  `python3 judge.py airline-ticket-concat`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    static void strcat(char[] result, char[] str1, char[] str2) {\n        // Write your code here ...\n\n    }\n}\n"
  },
  "assignment44-analyze-sentence": {
    "id": "assignment44-analyze-sentence",
    "title": "Assignment44 - Analyze Sentence",
    "summary": "Return the **number of words** of a sentence as a String. If the sentence contains digits it is invalid -> return `Invalid Sentence`.",
    "readme": "# Assignment44 - Analyze Sentence\n\n*Source: Practice-Test 13*\n\nReturn the **number of words** of a sentence as a String. If the sentence contains digits it is invalid -> return `Invalid Sentence`.\n\n`public static String analyzeSentence(String sentence)` in `class Main`\n\n`Java is powerful` -> `3`, `Java is powerful123` -> `Invalid Sentence`\n\nEdit `Solution.java`, then run:  `python3 judge.py assignment44-analyze-sentence`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static String analyzeSentence(String sentence)\n    {\n        // Students will implement this function\n        return \"\";\n    }\n}\n"
  },
  "class-box": {
    "id": "class-box",
    "title": "class - Box",
    "summary": "Design `class Box` with **private integer** `length`, `breadth`, `height`.",
    "readme": "# class - Box\n\n*Source: Practice-Test 10*\n\nDesign `class Box` with **private integer** `length`, `breadth`, `height`.\n\n- default constructor -> all 0\n- `Box(int length, int breadth, int height)`\n- copy constructor `Box(Box b1)`\n- `int getLength()`, `int getBreadth()`, `int getHeight()`\n- `long CalculateVolume()`\n\nSample: `3 4 5` -> default `0 0 0 0`, parameterised `3 4 5 60`, copy `3 4 5 60`.\nConstraints: `0 <= dimension <= 10^5` (watch the overflow of the volume!)\n\nEdit `Solution.java`, then run:  `python3 judge.py class-box`\n",
    "solution": "import java.util.Scanner;\n\nclass Box {\n    private int length, breadth, height;\n\n    Box() {\n        // Write your code here\n    }\n\n    Box(int length, int breadth, int height) {\n        // Write your code here\n    }\n\n    Box(Box b1) {\n        // Write your code here\n    }\n\n    int getLength() {\n        return 0;\n    }\n\n    int getBreadth() {\n        return 0;\n    }\n\n    int getHeight() {\n        return 0;\n    }\n\n    long CalculateVolume() {\n        return 0;\n    }\n}\n"
  },
  "class-student": {
    "id": "class-student",
    "title": "Class Student",
    "summary": "Design `class Student`:",
    "readme": "# Class Student\n\n*Source: Practice-Test 8*\n\nDesign `class Student`:\n\n| Member | Behaviour |\n|---|---|\n| `Student(int studentId, String name, int[] marks)` | initialise (5 marks) |\n| `void printValues()` | line 1 id, line 2 name, line 3 the five marks space-separated |\n| `int calTotalMarks()` | sum of the five marks |\n| `int secondMaxMarks()` | second highest mark |\n\nSample: `14 / Deepak Singh / 57 85 45 86 95` -> total `368`, second highest `86`.\n\nEdit `Solution.java`, then run:  `python3 judge.py class-student`\n",
    "solution": "import java.util.*;\n\nclass Student {\n    private int studentId;\n    private String name;\n    private int[] marks;\n\n    // Constructor\n    public Student(int studentId, String name, int[] marks) {\n\n    }\n\n    public void printValues() {\n\n    }\n\n    public int calTotalMarks() {\n        return 0;\n    }\n\n    public int secondMaxMarks() {\n        return 0;\n    }\n}\n"
  },
  "cloud-server-health": {
    "id": "cloud-server-health",
    "title": "Cloud Server Health Monitoring",
    "summary": "A server is **overloaded** when CPU utilisation is **>= 80**. Return the overloaded values in their original order.",
    "readme": "# Cloud Server Health Monitoring\n\n*Source: Practice-Test 11*\n\nA server is **overloaded** when CPU utilisation is **>= 80**. Return the overloaded values in their original order.\n\n`public static ArrayList<Integer> findOverloadedServers(ArrayList<Integer> cpuUsage)` in `class Main`\n\n`45 82 67 95 79 88 60` -> `82 95 88`\n\nEdit `Solution.java`, then run:  `python3 judge.py cloud-server-health`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static ArrayList<Integer>\n    findOverloadedServers(ArrayList<Integer> cpuUsage) {\n        // Write your code here\n        return new ArrayList<Integer>();\n    }\n}\n"
  },
  "college-seats-reserved": {
    "id": "college-seats-reserved",
    "title": "College Seats Are Reserved",
    "summary": "`A[i]` is the age for which seat `i` is reserved, `B[i]` the age of applicant `i`. Return `true` if **every seat can be filled** (both arrays contain the same ages with the same frequencies, in any order).",
    "readme": "# College Seats Are Reserved\n\n*Source: Practice-Test 14*\n\n`A[i]` is the age for which seat `i` is reserved, `B[i]` the age of applicant `i`. Return `true` if **every seat can be filled** (both arrays contain the same ages with the same frequencies, in any order).\n\n`static boolean allSeatsFilled(int[] A, int[] B)` in `class Result`\n\n`[11,12,13,12,13]` / `[12,13,11,12,13]` -> YES, `[11,12,13]` / `[12,13,12]` -> NO\n\nConstraints: `1 <= N <= 10^5`, `1 <= A[i], B[i] <= 100`\n\nEdit `Solution.java`, then run:  `python3 judge.py college-seats-reserved`\n",
    "solution": "import java.io.*;\nimport java.math.*;\nimport java.util.*;\n\nclass Result {\n    // Return true or false based on the fact, whether all the seats will be filled\n    static boolean allSeatsFilled(int[] A, int[] B) {\n        // Write your code here\n        return false;\n    }\n}\n"
  },
  "compress-a-string": {
    "id": "compress-a-string",
    "title": "Compress a string",
    "summary": "Compress a string: every run of the same character longer than 1 is replaced by the character followed by the run length. Single characters stay unchanged.",
    "readme": "# Compress a string\n\n*Source: Practice-Test 5*\n\nCompress a string: every run of the same character longer than 1 is replaced by the character followed by the run length. Single characters stay unchanged.\n\n`public static String compressString(String str)` in `class Main`\n\n`aabbccdef` -> `a2b2c2def`, `abddddddd` -> `abd7`\n\nEdit `Solution.java`, then run:  `python3 judge.py compress-a-string`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static String compressString(String str) {\n        //write your code here\n        return \"\";\n    }\n}\n"
  },
  "count-pos-neg-even-odd": {
    "id": "count-pos-neg-even-odd",
    "title": "Count negative, positive, even and odd",
    "summary": "Given an array of 10 integers, print four lines: the count of **positive**, **negative**, **even** and **odd** elements (zero is even, neither positive nor negative).",
    "readme": "# Count negative, positive, even and odd\n\n*Source: Practice-Test 2*\n\nGiven an array of 10 integers, print four lines: the count of **positive**, **negative**, **even** and **odd** elements (zero is even, neither positive nor negative).\n\n`static void countAndPrint(int[] arr, int n)` in `class Result`\n\nInput `-3 10 20 -4 7 1 -2 3 4 5` -> `7`, `3`, `5`, `5` (one per line)\n\nEdit `Solution.java`, then run:  `python3 judge.py count-pos-neg-even-odd`\n",
    "solution": "import java.util.Scanner;\n\nclass Result {\n    static void countAndPrint(int[] arr, int n) {\n        // write your code here\n    }\n}\n"
  },
  "custom-exception-power": {
    "id": "custom-exception-power",
    "title": "Calculate positive power of a positive number",
    "summary": "Write `class CustomException extends Exception` with a private `String msg`, constructor `CustomException(String message)` and an overridden `String getMessage()` returning the stored message.",
    "readme": "# Calculate positive power of a positive number\n\n*Source: Practice-Test 15*\n\nWrite `class CustomException extends Exception` with a private `String msg`, constructor `CustomException(String message)` and an overridden `String getMessage()` returning the stored message.\nThen implement `static int power(int num, int exp) throws CustomException` in `class Main`:\n\n1. if `num` or `exp` is negative -> throw `CustomException(\"Negative numbers not allowed\")`\n2. else if both are zero -> throw `CustomException(\"Both can never be zero\")`\n3. otherwise return `num^exp`\n\n`-4 -5` -> `Negative numbers not allowed`, `2 2` -> `4`\n\nEdit `Solution.java`, then run:  `python3 judge.py custom-exception-power`\n",
    "solution": "import java.util.Scanner;\n// You can add other imports below\n\n//DO NOT CHANGE CLASS NAME\nclass CustomException extends Exception {\n    // Write Your Code Here\n\n}\n\n//DO NOT CHANGE CLASS NAME\nclass Main {\n\n    static int power(int num, int exp) throws CustomException {\n        // Write Your Code Here\n\n        return 0;\n    }\n}\n"
  },
  "daily-loss-counter": {
    "id": "daily-loss-counter",
    "title": "The Daily Loss Counter",
    "summary": "Count the days with a **loss**, i.e. net performance strictly less than 0.",
    "readme": "# The Daily Loss Counter\n\n*Source: Practice-Test 5, 13*\n\nCount the days with a **loss**, i.e. net performance strictly less than 0.\n\n`public static int count(int[] a, int T)` in `class Solution`\n\n`1 2 3 -5` -> `1`\n\nConstraints: `1 <= T <= 1000`, `-10^6 <= a[i] <= 10^6`\n\nEdit `Solution.java`, then run:  `python3 judge.py daily-loss-counter`\n",
    "solution": "import java.util.*;\nimport java.io.*;\n\n// Do NOT change the class name\nclass Solution {\n    public static int count(int[] a, int T) {\n        // Write your code here\n        return 0;\n    }\n}\n"
  },
  "date-class": {
    "id": "date-class",
    "title": "Implement the Date class",
    "summary": "Implement `class Date` for a **non-leap year** (Feb always has 28 days). The year is not stored.",
    "readme": "# Implement the Date class\n\n*Source: Practice-Test 6*\n\nImplement `class Date` for a **non-leap year** (Feb always has 28 days). The year is not stored.\n\n| Member | Behaviour |\n|---|---|\n| `private int month, date` | 1-12 and day of month |\n| `Date()` | January 1st |\n| `Date(int m, int d)` | sets month and day |\n| `int daysInMonth()` | days in the current month (31 for Jan, 28 for Feb ...) |\n| `int getDay()` / `int getMonth()` | current values |\n| `void nextDay()` | +1 day, wraps to 1st of next month, Dec 31 -> Jan 1 |\n\nNo `main` needed.\n\nEdit `Solution.java`, then run:  `python3 judge.py date-class`\n",
    "solution": "class Date {\n    private int month;\n    private int date;\n\n    public Date() {\n\n    }\n\n    public Date(int month, int date) {\n\n    }\n\n    public int getMonth() {\n        return 0;\n    }\n\n    public int getDay() {\n        return 0;\n    }\n\n    public int daysInMonth() {\n        return 0;\n    }\n\n    public void nextDay() {\n\n    }\n}\n"
  },
  "employee": {
    "id": "employee",
    "title": "Employee",
    "summary": "Track six months of salaries for an employee.",
    "readme": "# Employee\n\n*Source: Practice-Test 7*\n\nTrack six months of salaries for an employee.\n\n| Method | Behaviour |\n|---|---|\n| `void getValues(int id, String name, int[] salary)` | store the data |\n| `void printValues()` | print id, name (may contain spaces), the six salaries space-separated - 3 lines |\n| `int calTotalSalary()` | sum of the six salaries |\n| `int maxSalary()` | month number (1-6) of the highest salary |\n\nSample: `3234 / Nitin Kumar / 12313 12001 10333 14923 15783 10010` -> total `75363`, max in month `5`.\n\nEdit `Solution.java`, then run:  `python3 judge.py employee`\n",
    "solution": "import java.util.Scanner;\n\nclass Employee {\n    private int e_Id;\n    private String name;\n    private int[] salary = new int[6];\n\n    public void getValues(int id, String name, int[] salary) {\n\n    }\n\n    public void printValues() {}\n\n    public int calTotalSalary() {\n        return 0;\n    }\n\n    public int maxSalary() {\n        return 0;\n    }\n}\n"
  },
  "exam-topper": {
    "id": "exam-topper",
    "title": "Exam Topper",
    "summary": "Given the marks of `N` students, return the **maximum** marks scored by any student.",
    "readme": "# Exam Topper\n\n*Source: Practice-Test 1, 12*\n\nGiven the marks of `N` students, return the **maximum** marks scored by any student.\n\n`static int maxMarks(int[] marks, int N)` in `class Result`\n\nConstraints: `1 <= N <= 10^5`, `-1000 <= marks[i] <= 1000`\n\n| Input | Output |\n|---|---|\n| `20 30 93 71 18 82 66` | `93` |\n| `33 45 67 33 67` | `67` |\n\nEdit `Solution.java`, then run:  `python3 judge.py exam-topper`\n",
    "solution": "import java.util.*;\n\nclass Result {\n    static int maxMarks(int[] marks, int N) {\n        // Write Your Code here\n        return 0;\n    }\n}\n"
  },
  "find-the-longest-word": {
    "id": "find-the-longest-word",
    "title": "Find the Longest Word",
    "summary": "Return the longest word in a sentence (letters and single spaces only, no leading/trailing spaces).",
    "readme": "# Find the Longest Word\n\n*Source: Practice-Test 7*\n\nReturn the longest word in a sentence (letters and single spaces only, no leading/trailing spaces).\n\n`public static String findLongestWord(String input)` in `class Main`\n\n`I love programming` -> `programming`\n\nConstraints: sentence length <= 10^5 (tests have a unique longest word)\n\nEdit `Solution.java`, then run:  `python3 judge.py find-the-longest-word`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static String findLongestWord(String input) {\n        // Write Your Code Here\n        return \"\";\n    }\n}\n"
  },
  "layered-pyramid-3": {
    "id": "layered-pyramid-3",
    "title": "Layered Calibration Code Pyramid - 3",
    "summary": "Read `n`. Row `i` (1..n) prints `n-i` stars followed by `1..i` (no spaces).",
    "readme": "# Layered Calibration Code Pyramid - 3\n\n*Source: Practice-Test 5*\n\nRead `n`. Row `i` (1..n) prints `n-i` stars followed by `1..i` (no spaces).\n\nInput `5` ->\n```\n****1\n***12\n**123\n*1234\n12345\n```\n\nEdit `Solution.java`, then run:  `python3 judge.py layered-pyramid-3`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // write your code here\n    }\n}\n"
  },
  "library-book-inventory": {
    "id": "library-book-inventory",
    "title": "Library Book Inventory Management",
    "summary": "Add each newly arrived book id to the inventory **only if it is not already present** (duplicates inside `newBooks` also count). Return the updated `ArrayList`.",
    "readme": "# Library Book Inventory Management\n\n*Source: Practice-Test 15*\n\nAdd each newly arrived book id to the inventory **only if it is not already present** (duplicates inside `newBooks` also count). Return the updated `ArrayList`.\n\n`public static ArrayList<Integer> updateInventory(ArrayList<Integer> books, int[] newBooks)` in `class Main`\n\n`101 102 103 104` + `104 105 106 102 107` -> `101 102 103 104 105 106 107`\n\nEdit `Solution.java`, then run:  `python3 judge.py library-book-inventory`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static ArrayList<Integer>\n    updateInventory(ArrayList<Integer> books, int[] newBooks) {\n        //write your code here\n        return null;\n    }\n}\n"
  },
  "lowercase-to-uppercase": {
    "id": "lowercase-to-uppercase",
    "title": "Convert lower case to upper case",
    "summary": "Read a string of lowercase letters (a-z, length 1..1000) and print it in uppercase.",
    "readme": "# Convert lower case to upper case\n\n*Source: Practice-Test 4*\n\nRead a string of lowercase letters (a-z, length 1..1000) and print it in uppercase.\n\n`codequotient` -> `CODEQUOTIENT`\n\nEdit `Solution.java`, then run:  `python3 judge.py lowercase-to-uppercase`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // Write your code here\n    }\n}\n"
  },
  "main-diagonal-sum": {
    "id": "main-diagonal-sum",
    "title": "Find sum of main diagonal of matrix",
    "summary": "Return the sum of the main diagonal of an `m x m` matrix.",
    "readme": "# Find sum of main diagonal of matrix\n\n*Source: Practice-Test 9*\n\nReturn the sum of the main diagonal of an `m x m` matrix.\n\n`public static int mainDiagonalSum(int[][] matrix, int m)` in `class Main`\n\n`[[1,2,3],[4,5,6],[7,8,9]]` -> `1+5+9 = 15`\n\nEdit `Solution.java`, then run:  `python3 judge.py main-diagonal-sum`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static int mainDiagonalSum(int[][] matrix, int m) {\n        //write your code here\n        return 0;\n    }\n}\n"
  },
  "matrix-multiplication": {
    "id": "matrix-multiplication",
    "title": "Matrix Multiplication",
    "summary": "Multiply `A (R1 x C1)` by `B (C1 x C2)` and return the `R1 x C2` result.",
    "readme": "# Matrix Multiplication\n\n*Source: Practice-Test 7*\n\nMultiply `A (R1 x C1)` by `B (C1 x C2)` and return the `R1 x C2` result.\n\n`public static int[][] multiply(int[][] A, int[][] B, int R1, int C1, int C2)` in `class Main`\n\n`[[1,2,3],[4,5,6]] x [[2,3],[1,2],[2,1]]` -> `[[10,10],[25,28]]`\n\nConstraints: `-1000 <= elements <= 1000`\n\nEdit `Solution.java`, then run:  `python3 judge.py matrix-multiplication`\n",
    "solution": "class Main {\n    public static int[][] multiply(int[][] A, int[][] B, int R1, int C1, int C2) {\n        // write your code here\n        return null;\n    }\n}\n"
  },
  "matrix-row-and-column-sum": {
    "id": "matrix-row-and-column-sum",
    "title": "Sum of elements of matrix",
    "summary": "Read `rows`, `cols`, the matrix, a row index `r` and a column index `c` (0-based). Print **sum(row r) + sum(column c)**",
    "readme": "# Sum of elements of matrix\n\n*Source: Practice-Test 6*\n\nRead `rows`, `cols`, the matrix, a row index `r` and a column index `c` (0-based). Print **sum(row r) + sum(column c)**\n(the element at `[r][c]` is counted twice).\n\nInput\n```\n2\n3\n1 2 3\n4 5 6\n0\n0\n```\nOutput `11`  (row0 = 6, col0 = 5)\n\nEdit `Solution.java`, then run:  `python3 judge.py matrix-row-and-column-sum`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // Write your code here\n    }\n}\n"
  },
  "mycalculator-exception": {
    "id": "mycalculator-exception",
    "title": "MyCalculator Exception",
    "summary": "`class MyException extends Exception` (with an `int code`) is provided. Implement `static void power(int n, int p)` in `class Main` that **throws, catches (inside `power`) and prints the error code**:",
    "readme": "# MyCalculator Exception\n\n*Source: Practice-Test 12*\n\n`class MyException extends Exception` (with an `int code`) is provided. Implement `static void power(int n, int p)` in `class Main` that **throws, catches (inside `power`) and prints the error code**:\n\n1. if `n` or `p` is negative -> throw `MyException(-1)` -> print `-1`\n2. else if both are `0` -> throw `MyException(-2)` -> print `-2`\n3. otherwise print `n^p`\n\nInput `2 3` `-3 2` `0 0` `5 0` `0 5` -> `8 -1 -2 1 0` (one per line)\n\nEdit `Solution.java`, then run:  `python3 judge.py mycalculator-exception`\n",
    "solution": "import java.util.Scanner;\n\nclass MyException extends Exception {\n    int code;\n\n    MyException(int code) {\n        this.code = code;\n    }\n}\n\nclass Main {\n    static void power(int n, int p) {\n        //write your code here\n    }\n}\n"
  },
  "perfect-string": {
    "id": "perfect-string",
    "title": "Perfect String",
    "summary": "A string made only of `a`, `b`, `x`, `y` is **perfect** if the number of `a`+`b` characters is **odd** and the number of `x`+`y` characters is **even**.",
    "readme": "# Perfect String\n\n*Source: Practice-Test 8*\n\nA string made only of `a`, `b`, `x`, `y` is **perfect** if the number of `a`+`b` characters is **odd** and the number of `x`+`y` characters is **even**.\n\n`public static boolean isPerfect(String str)` in `class Result`\n\n`xaxbyyb` (3 / 4) -> YES, `aabbxxyy` (4 / 4) -> NO, `abaabxy` (5 / 2) -> YES, `yyxaby` (2 / 4) -> NO\n\nEdit `Solution.java`, then run:  `python3 judge.py perfect-string`\n",
    "solution": "import java.io.*;\nimport java.util.*;\n\nclass Result {\n    /*\n     * Complete the 'isPerfect' function below.\n     * @params str -> a string that is to be tested\n     * @return boolean value, whether the given string is perfect or not.\n     */\n    public static boolean isPerfect(String str) {\n        // Write your code here\n        return false;\n    }\n}\n"
  },
  "pyramid-13": {
    "id": "pyramid-13",
    "title": "Pyramid - 13",
    "summary": "Read `n` and print `n` rows: row 1 has `n` stars, each next row has one star fewer (last row has 1 star).",
    "readme": "# Pyramid - 13\n\n*Source: Practice-Test 1*\n\nRead `n` and print `n` rows: row 1 has `n` stars, each next row has one star fewer (last row has 1 star).\n\nConstraints: `1 <= n <= 50`\n\nInput `5` ->\n```\n*****\n****\n***\n**\n*\n```\n\nEdit `Solution.java`, then run:  `python3 judge.py pyramid-13`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // write your code here\n    }\n}\n"
  },
  "pyramid-4": {
    "id": "pyramid-4",
    "title": "Pyramid - 4",
    "summary": "Read `n`. Row `i` (1..n) prints `n-i` stars followed by the numbers `i, i-1, ... 1` (no spaces).",
    "readme": "# Pyramid - 4\n\n*Source: Practice-Test 2*\n\nRead `n`. Row `i` (1..n) prints `n-i` stars followed by the numbers `i, i-1, ... 1` (no spaces).\n\nInput `5` ->\n```\n****1\n***21\n**321\n*4321\n54321\n```\n\nEdit `Solution.java`, then run:  `python3 judge.py pyramid-4`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // write your code here\n    }\n}\n"
  },
  "pyramid-9": {
    "id": "pyramid-9",
    "title": "Pyramid - 9",
    "summary": "Day 1 has items `1..n`. Each following day the last item is removed. Print the row for every day.",
    "readme": "# Pyramid - 9\n\n*Source: Practice-Test 3*\n\nDay 1 has items `1..n`. Each following day the last item is removed. Print the row for every day.\n\nInput `3` ->\n```\n123\n12\n1\n```\n\nEdit `Solution.java`, then run:  `python3 judge.py pyramid-9`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // write your code here\n    }\n}\n"
  },
  "quality-check": {
    "id": "quality-check",
    "title": "Quality Check (even / odd count)",
    "summary": "Given `T` integers, print the count of **even** and **odd** elements on one line separated by a space (even first).",
    "readme": "# Quality Check (even / odd count)\n\n*Source: Practice-Test 4, 11*\n\nGiven `T` integers, print the count of **even** and **odd** elements on one line separated by a space (even first).\n\n`static void count(int[] a, int T)` in `class Solution`\n\n`1 3 5 8` -> `1 3`\n\nConstraints: `1 <= T <= 100`, `1 <= a[i] <= 10^5`\n\nEdit `Solution.java`, then run:  `python3 judge.py quality-check`\n",
    "solution": "import java.util.*;\n\nclass Solution {\n    static void count(int[] a, int T) {\n        //write your code here\n    }\n}\n"
  },
  "save-bandwidth-compression": {
    "id": "save-bandwidth-compression",
    "title": "Save Bandwidth Using Compression",
    "summary": "Compress a text message: each **consecutive run** of a character longer than 1 becomes `char + count`.",
    "readme": "# Save Bandwidth Using Compression\n\n*Source: Practice-Test 6*\n\nCompress a text message: each **consecutive run** of a character longer than 1 becomes `char + count`.\n\n`static String compressMsg(String textMsg)` in `class Result`\n\n`ggkkgdddgggg` -> `g2k2gd3g4`, `abddddddd` -> `abd7`\n\nEdit `Solution.java`, then run:  `python3 judge.py save-bandwidth-compression`\n",
    "solution": "import java.util.*;\n\nclass Result {\n    // return the compressed string\n    static String compressMsg(String textMsg) {\n        // Write your code here\n        return \"\";\n    }\n}\n"
  },
  "search-an-element": {
    "id": "search-an-element",
    "title": "Search an element",
    "summary": "An array has a fixed size of 7. Return the **number of times** `ele` occurs in it, or `-1` if it is not present.",
    "readme": "# Search an element\n\n*Source: Practice-Test 3, 15*\n\nAn array has a fixed size of 7. Return the **number of times** `ele` occurs in it, or `-1` if it is not present.\n\n`static int SearchElement(int[] arr, int ele)` in `class Search`\n\nArray `3 10 20 4 7 4 5`: `4` -> `2`, `5` -> `1`, `6` -> `-1`\n\nEdit `Solution.java`, then run:  `python3 judge.py search-an-element`\n",
    "solution": "import java.util.Scanner;\n\nclass Search {\n    static int SearchElement(int[] arr, int ele) {\n        //write your code here\n        return 0;\n    }\n}\n"
  },
  "separate-even-odd": {
    "id": "separate-even-odd",
    "title": "Put even and odd elements in 2 separate arrays",
    "summary": "Split the array into an array of even elements and an array of odd elements (keep the original order), then **print** the even elements on the first line and the odd elements on the second line, space-separated. Do not read input.",
    "readme": "# Put even and odd elements in 2 separate arrays\n\n*Source: Practice-Test 14*\n\nSplit the array into an array of even elements and an array of odd elements (keep the original order), then **print** the even elements on the first line and the odd elements on the second line, space-separated. Do not read input.\n\n`static void separate(int a[], int n)` in `class Main`\n\n`1 3 5 8` -> `8` / `1 3 5`\n\nConstraints: `1 <= n <= 100`, `-10^9 <= a[i] <= 10^9` (negative odd numbers exist!)\n\nEdit `Solution.java`, then run:  `python3 judge.py separate-even-odd`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    // This function separates the elements of the array into even and odd.\n    // It prints all even elements in the first line and odd elements in the second line.\n    static void separate(int a[], int n) {\n        // write your code here.\n    }\n}\n"
  },
  "sequential-id-pyramid-7": {
    "id": "sequential-id-pyramid-7",
    "title": "Sequential ID Pyramid - 7",
    "summary": "Read `n`. Row `i` has `i` consecutive ids, continuing the counter from the previous row. Separate numbers in a row with a single space.",
    "readme": "# Sequential ID Pyramid - 7\n\n*Source: Practice-Test 4*\n\nRead `n`. Row `i` has `i` consecutive ids, continuing the counter from the previous row. Separate numbers in a row with a single space.\n\nInput `3` ->\n```\n1\n2 3\n4 5 6\n```\nConstraints: `1 <= n <= 50`\n\nEdit `Solution.java`, then run:  `python3 judge.py sequential-id-pyramid-7`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // write your code here\n    }\n}\n"
  },
  "stock-price-trend": {
    "id": "stock-price-trend",
    "title": "Stock Trading - Price Trend Analyzer",
    "summary": "Return a **new** `LinkedList` with every price that is **strictly greater** than the previous trading session's price (the first price is ignored). Keep the original order, do not modify the input, empty list if none.",
    "readme": "# Stock Trading - Price Trend Analyzer\n\n*Source: Practice-Test 13*\n\nReturn a **new** `LinkedList` with every price that is **strictly greater** than the previous trading session's price (the first price is ignored). Keep the original order, do not modify the input, empty list if none.\n\n`public static LinkedList<Integer> findIncreasingPrices(LinkedList<Integer> prices)` in `class Main`\n\n`500 520 510 550 550 580 560` -> `520 550 580`\n\nEdit `Solution.java`, then run:  `python3 judge.py stock-price-trend`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static LinkedList<Integer>\n    findIncreasingPrices(LinkedList<Integer> prices) {\n\n        // Write your code here\n        return null;\n    }\n}\n"
  },
  "strings-are-anagram": {
    "id": "strings-are-anagram",
    "title": "Strings are anagram or not",
    "summary": "Two strings are **anagrams** if they contain the same characters (case matters) with the same frequencies. Return `1` if anagram, else `0`.",
    "readme": "# Strings are anagram or not\n\n*Source: Practice-Test 9*\n\nTwo strings are **anagrams** if they contain the same characters (case matters) with the same frequencies. Return `1` if anagram, else `0`.\n\n`static int isAnagram(String str1, String str2)` in `class Main`\n\n`act`/`cat` -> 1, `CodeQuotient`/`QuotientCode` -> 1, `Hello`/`Hillo` -> 0\n\nEdit `Solution.java`, then run:  `python3 judge.py strings-are-anagram`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    static int isAnagram(String str1, String str2) {\n        // Write your code here\n        return 0;\n    }\n}\n"
  },
  "strong-virus": {
    "id": "strong-virus",
    "title": "Strong Virus Detection",
    "summary": "A DNA sequence (any printable ASCII, may contain spaces) describes a virus. The virus is **strong** if it has an",
    "readme": "# Strong Virus Detection\n\n*Source: Practice-Test 1*\n\nA DNA sequence (any printable ASCII, may contain spaces) describes a virus. The virus is **strong** if it has an\n`x` and a `y` with **exactly three characters between them**. Return `true` if strong, else `false`.\n\n`boolean isStrongVirus(String dna)` in `class Virus` (instance method)\n\nExample: `txma yert` -> x at index 1, y at index 5, between them `m`, `a`, ` ` -> **YES**\n`BMuxp ioqytB yxurN` -> **NO**, `xaxoerylm` -> **YES**\n\nTotal length of all sequences <= 10^6.\n\nEdit `Solution.java`, then run:  `python3 judge.py strong-virus`\n",
    "solution": "class Virus {\n    // Returns true if the virus is strong, otherwise false\n    boolean isStrongVirus(String dna) {\n        // Write your code here\n        return false;\n    }\n}\n"
  },
  "student-marks-get-element": {
    "id": "student-marks-get-element",
    "title": "Student Marks Management System",
    "summary": "Return the element at `index` as a **String**. If the index is invalid, **handle the exception** and return `Invalid Index`.",
    "readme": "# Student Marks Management System\n\n*Source: Practice-Test 14*\n\nReturn the element at `index` as a **String**. If the index is invalid, **handle the exception** and return `Invalid Index`.\n\n`public static String getElement(int arr[], int index)` in `class Main`\n\n`10 20 30 40 50`, index `2` -> `30`; index `7` -> `Invalid Index`\n\nEdit `Solution.java`, then run:  `python3 judge.py student-marks-get-element`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static String getElement(int arr[], int index)\n    {\n        // Students will implement this function\n        return \"\";\n    }\n}\n"
  },
  "sum-lower-triangle": {
    "id": "sum-lower-triangle",
    "title": "Sum of Lower Triangle of a Square Matrix",
    "summary": "Read `N` and an `N x N` matrix. Print the sum of the **lower triangle including the main diagonal** (elements with `col <= row`).",
    "readme": "# Sum of Lower Triangle of a Square Matrix\n\n*Source: Practice-Test 10*\n\nRead `N` and an `N x N` matrix. Print the sum of the **lower triangle including the main diagonal** (elements with `col <= row`).\n\n```\n3\n1 2 3\n4 5 6\n7 8 9\n```\nOutput `34` (1 + 4 + 5 + 7 + 8 + 9)\n\nConstraints: `1 <= N <= 5`, `-100 <= matrix[i][j] <= 100`\n\nEdit `Solution.java`, then run:  `python3 judge.py sum-lower-triangle`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // Write your code here\n    }\n}\n"
  },
  "sum-of-kth-row": {
    "id": "sum-of-kth-row",
    "title": "Sum of Elements in the Kth Row of a Matrix",
    "summary": "Read `R C`, the `R x C` matrix, then `K` (0-based). Print the sum of row `K`.",
    "readme": "# Sum of Elements in the Kth Row of a Matrix\n\n*Source: Practice-Test 8*\n\nRead `R C`, the `R x C` matrix, then `K` (0-based). Print the sum of row `K`.\n\n```\n3 5\n1 3 5 7 9\n2 4 6 8 10\n2 6 9 3 4\n2\n```\nOutput `24`\n\nConstraints: `1 <= R,C <= 100`, `0 <= K < R`, `-1000 <= matrix[i][j] <= 1000`\n\nEdit `Solution.java`, then run:  `python3 judge.py sum-of-kth-row`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String args[]) {\n        // Write your code here\n    }\n}\n"
  },
  "translate-the-letter": {
    "id": "translate-the-letter",
    "title": "Translate The Letter",
    "summary": "Reverse the **order of the words** in a sentence (words are separated by exactly one space, no leading/trailing spaces).",
    "readme": "# Translate The Letter\n\n*Source: Practice-Test 2*\n\nReverse the **order of the words** in a sentence (words are separated by exactly one space, no leading/trailing spaces).\n\n`static String translate(String letter)` in `class Result`\n\n`Code Loves Quotient Code` -> `Code Quotient Loves Code`\n`Coders Hello` -> `Hello Coders`\n\nConstraints: sentence length <= 100000\n\nEdit `Solution.java`, then run:  `python3 judge.py translate-the-letter`\n",
    "solution": "import java.util.*;\n\nclass Result {\n    static String translate(String letter) {\n        // Write your code here\n        return \"\";\n    }\n}\n"
  },
  "tricycle-speed-manager": {
    "id": "tricycle-speed-manager",
    "title": "Tricycle Speed Manager",
    "summary": "`class Tricycle` with `private int speed`.",
    "readme": "# Tricycle Speed Manager\n\n*Source: Practice-Test 9*\n\n`class Tricycle` with `private int speed`.\n\n| Member | Behaviour |\n|---|---|\n| `Tricycle()` | speed = 5 |\n| `Tricycle(Tricycle t)` | copy of `t`'s speed (independent object) |\n| `void setSpeed(int s)` / `int getSpeed()` | set / get |\n| `void incr()` / `void brake()` | speed +1 / -1 |\n\nDriver: t1 default, incr; t2 = copy of t1, incr, setSpeed(x); brake both.\n\nEdit `Solution.java`, then run:  `python3 judge.py tricycle-speed-manager`\n",
    "solution": "import java.util.Scanner;\n\nclass Tricycle {\n    private int speed;\n\n    public Tricycle() {\n\n    }\n\n    public Tricycle(Tricycle t) {\n\n    }\n\n    public void setSpeed(int s) {\n\n    }\n\n    public int getSpeed() {\n        return 0;\n    }\n\n    public void incr() {\n\n    }\n\n    public void brake() {\n\n    }\n}\n"
  },
  "uppercase-to-lowercase": {
    "id": "uppercase-to-lowercase",
    "title": "Convert Uppercase String to Lowercase",
    "summary": "Read a string of uppercase letters (A-Z, length 1..1000) and print it in lowercase.",
    "readme": "# Convert Uppercase String to Lowercase\n\n*Source: Practice-Test 3*\n\nRead a string of uppercase letters (A-Z, length 1..1000) and print it in lowercase.\n\n`CODEQUOTIENT` -> `codequotient`\n\nEdit `Solution.java`, then run:  `python3 judge.py uppercase-to-lowercase`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // Write your code here\n    }\n}\n"
  },
  "valid-email-address": {
    "id": "valid-email-address",
    "title": "Valid email address",
    "summary": "Validate an email. It is **valid** only if it has exactly one `@`, exactly one `.`, the `.` comes **after** the `@`, and there is at least one character between `@` and `.`.",
    "readme": "# Valid email address\n\n*Source: Practice-Test 11*\n\nValidate an email. It is **valid** only if it has exactly one `@`, exactly one `.`, the `.` comes **after** the `@`, and there is at least one character between `@` and `.`.\nThrow the user-defined `EmailException` for an invalid address, **catch it inside** `isValidEmail`, and print `1` (valid) or `0` (invalid).\n\n`static void isValidEmail(String email)` in `class Main`\n\n`abc@gmail.com` -> 1, `email@codequotient` -> 0, `user.name@domain` -> 0, `student@college.edu` -> 1\n\nEdit `Solution.java`, then run:  `python3 judge.py valid-email-address`\n",
    "solution": "import java.util.Scanner;\n\nclass EmailException extends Exception {\n    EmailException() {\n        super();\n    }\n}\n\nclass Main {\n    static void isValidEmail(String email) {\n        //write your code here\n    }\n}\n"
  },
  "web-browser-tab-history": {
    "id": "web-browser-tab-history",
    "title": "Web Browser Tab History Analyzer",
    "summary": "Given a `LinkedList<Integer>` of website ids, return a **new** `LinkedList` of ids that appear **more than once**, each only once, in order of their **first appearance**. Do not modify the input. If none is frequent return an empty list.",
    "readme": "# Web Browser Tab History Analyzer\n\n*Source: Practice-Test 12*\n\nGiven a `LinkedList<Integer>` of website ids, return a **new** `LinkedList` of ids that appear **more than once**, each only once, in order of their **first appearance**. Do not modify the input. If none is frequent return an empty list.\n\n`public static LinkedList<Integer> findFrequentSites(LinkedList<Integer> history)` in `class Main`\n\n`101 205 310 101 450 205 101 520 310 600` -> `101 205 310`\n\nConstraints: `1 <= N <= 1000`, `100 <= id <= 999`\n\nEdit `Solution.java`, then run:  `python3 judge.py web-browser-tab-history`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static LinkedList<Integer>\n    findFrequentSites(LinkedList<Integer> history) {\n\n        // Write your code here\n        return null;\n    }\n}\n"
  }
}

import json
from pathlib import Path

_meta_candidates = [
    Path(__file__).resolve().parent.parent / "problems_meta.json",
    Path(__file__).resolve().parent / "problems_meta.json",
    Path.cwd() / "problems_meta.json",
]
_meta = {}
for _p in _meta_candidates:
    if _p.is_file():
        try:
            _meta = json.loads(_p.read_text(encoding="utf-8"))
            break
        except Exception:
            pass

for _pid, _pdata in PROBLEMS.items():
    _m = _meta.get(_pid, {})
    _pdata["difficulty"] = _m.get("difficulty", "Easy")
    _pdata["topics"] = _m.get("topics", [])
    _pdata["hints"] = _m.get("hints", [])
    _pdata["sample_cases"] = _m.get("sample_cases", [])

PATHS = [
    {
        "id": "java-basics",
        "name": "Java Basics & Control Flow",
        "tier": "Fundamental",
        "icon": "☕",
        "description": "Master variables, loops, conditionals, and standard I/O in core Java.",
    },
    {
        "id": "arrays-and-strings",
        "name": "Arrays & Strings Mastery",
        "tier": "Core",
        "icon": "🔡",
        "description": "Index manipulation, string transformations, anagrams, and frequency counting.",
    },
    {
        "id": "oop-mastery",
        "name": "Object-Oriented Programming",
        "tier": "Advanced",
        "icon": "📦",
        "description": "Constructors, encapsulation, member methods, inheritance, and custom classes.",
    },
    {
        "id": "exceptions-collections",
        "name": "Exceptions & Collections",
        "tier": "Interview-Ready",
        "icon": "⚡",
        "description": "Custom exceptions, try-catch hierarchies, ArrayLists, and LinkedLists.",
    },
]

COLLECTIONS = [
    {"id": "placement-favorites", "name": "Campus Placement Favorites", "count": 15},
    {"id": "oop-essentials", "name": "OOP Design Essentials", "count": 12},
    {"id": "arrays-matrix", "name": "Arrays & Matrix Challenges", "count": 14},
]

