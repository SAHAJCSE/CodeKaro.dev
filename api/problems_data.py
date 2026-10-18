"""Pre-bundled problem data for Vercel serverless execution."""

PATHS = [
  {
    "id": "java-basics",
    "name": "Java Basics",
    "description": "Syntax fundamentals, variables, conditional logic, and simple input/output."
  },
  {
    "id": "strings",
    "name": "Strings",
    "description": "String manipulation, character arrays, parsing, formatting, and pattern matching."
  },
  {
    "id": "loops-functions",
    "name": "Loops & Functions",
    "description": "Iteration, nested loops, star/digit patterns, modular function design."
  },
  {
    "id": "oop",
    "name": "OOP",
    "description": "Classes, constructors, encapsulation, object state, and exception handling."
  },
  {
    "id": "recursion",
    "name": "Recursion",
    "description": "Recursive decomposition, recursive tracking, and divide-and-conquer logic."
  },
  {
    "id": "sorting-searching",
    "name": "Sorting & Searching",
    "description": "Linear search, array transformations, matrix traversals, and ordering."
  }
]

COLLECTIONS = [
  {
    "id": "company-tcs",
    "name": "TCS NQT & Digital",
    "category": "Company",
    "description": "High-frequency coding problems asked in TCS Ninja and Digital assessments."
  },
  {
    "id": "company-infosys",
    "name": "Infosys DSE/SP",
    "category": "Company",
    "description": "Problem solving sets curated for Infosys Specialist Programmer hiring."
  },
  {
    "id": "company-wipro",
    "name": "Wipro Elite NTH",
    "category": "Company",
    "description": "Pattern, string, and array assessment challenges from Wipro Elite tests."
  },
  {
    "id": "company-capgemini",
    "name": "Capgemini Exceller",
    "category": "Company",
    "description": "OOP and algorithmic coding assessments frequently appearing in Capgemini drives."
  },
  {
    "id": "company-amazon",
    "name": "Amazon SDE",
    "category": "Company",
    "description": "Core data structure & object modeling interview problems."
  },
  {
    "id": "college-placement",
    "name": "Campus Placement Sets",
    "category": "College",
    "description": "Curated placement practice sets covering high-probability aptitude coding tests."
  },
  {
    "id": "college-cuiet-lab",
    "name": "Semester Lab Sets (CUIET)",
    "category": "College",
    "description": "Official laboratory assignments and evaluation problems from CUIET coursework."
  },
  {
    "id": "exam-gate",
    "name": "GATE CS & IT",
    "category": "Exam",
    "description": "Conceptual problems targeting programming methodology and complexity."
  },
  {
    "id": "exam-university",
    "name": "University Semester Exams",
    "category": "Exam",
    "description": "End-term theory and lab examination problems for Bachelor of Technology."
  },
  {
    "id": "exam-viva",
    "name": "OOP Viva Prep",
    "category": "Exam",
    "description": "Corner-case and constructor questions ideal for technical vivas."
  }
]

PROBLEMS = {
  "airline-ticket-concat": {
    "id": "airline-ticket-concat",
    "title": "The Airline Ticket - Concatenate two strings",
    "summary": "Concatenate two strings **without** `String.concat` / `+`: copy `str1` followed by `str2` into the char array `result` (it is at least `len1 + len2` long).",
    "readme": "# The Airline Ticket - Concatenate two strings\n\n*Source: Practice-Test 10*\n\nConcatenate two strings **without** `String.concat` / `+`: copy `str1` followed by `str2` into the char array `result` (it is at least `len1 + len2` long).\n\n`static void strcat(char[] result, char[] str1, char[] str2)` in `class Main`\n\n`Code` + `Quotient` -> `CodeQuotient`, `John` + `Doe` -> `JohnDoe`\n\nEdit `Solution.java`, then run:  `python3 judge.py airline-ticket-concat`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    static void strcat(char[] result, char[] str1, char[] str2) {\n        // Write your code here ...\n\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Strings",
      "Arrays"
    ],
    "hints": [
      "Do not use String.concat() or the '+' string concatenation operator.",
      "Copy characters of str1 from index 0 into result, then copy str2 directly following str1."
    ],
    "sample_cases": [
      {
        "name": "Code + Quotient",
        "input": "\"Code\", \"Quotient\", 0",
        "expected": "CodeQuotient"
      },
      {
        "name": "John + Doe",
        "input": "\"John\", \"Doe\", 0",
        "expected": "JohnDoe"
      },
      {
        "name": "single chars",
        "input": "\"a\", \"b\", 0",
        "expected": "ab"
      }
    ],
    "display_number": 1,
    "display_id": "01",
    "languages": [
      "Java"
    ],
    "path_id": "strings",
    "path_name": "Strings",
    "order_in_path": 1,
    "collection_ids": [
      "college-placement",
      "company-tcs",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "assignment44-analyze-sentence": {
    "id": "assignment44-analyze-sentence",
    "title": "Assignment44 - Analyze Sentence",
    "summary": "Return the **number of words** of a sentence as a String. If the sentence contains digits it is invalid -> return `Invalid Sentence`.",
    "readme": "# Assignment44 - Analyze Sentence\n\n*Source: Practice-Test 13*\n\nReturn the **number of words** of a sentence as a String. If the sentence contains digits it is invalid -> return `Invalid Sentence`.\n\n`public static String analyzeSentence(String sentence)` in `class Main`\n\n`Java is powerful` -> `3`, `Java is powerful123` -> `Invalid Sentence`\n\nEdit `Solution.java`, then run:  `python3 judge.py assignment44-analyze-sentence`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static String analyzeSentence(String sentence)\n    {\n        // Students will implement this function\n        return \"\";\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Strings",
      "Loops"
    ],
    "hints": [
      "Iterate through the characters of sentence using Character.isDigit(c). If any digit is found, return 'Invalid Sentence'.",
      "If valid, split the sentence by whitespace using sentence.trim().split(\"\\\\s+\") and return the length as a String."
    ],
    "sample_cases": [
      {
        "name": "sample 1",
        "input": "\"Java is powerful\"",
        "expected": "3"
      },
      {
        "name": "sample 2 (digits)",
        "input": "\"Java is powerful123\"",
        "expected": "Invalid Sentence"
      },
      {
        "name": "single word",
        "input": "\"Hello\"",
        "expected": "1"
      }
    ],
    "display_number": 2,
    "display_id": "02",
    "languages": [
      "Java"
    ],
    "path_id": "strings",
    "path_name": "Strings",
    "order_in_path": 2,
    "collection_ids": [
      "company-infosys",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "class-box": {
    "id": "class-box",
    "title": "class - Box",
    "summary": "Design `class Box` with **private integer** `length`, `breadth`, `height`.",
    "readme": "# class - Box\n\n*Source: Practice-Test 10*\n\nDesign `class Box` with **private integer** `length`, `breadth`, `height`.\n\n- default constructor -> all 0\n- `Box(int length, int breadth, int height)`\n- copy constructor `Box(Box b1)`\n- `int getLength()`, `int getBreadth()`, `int getHeight()`\n- `long CalculateVolume()`\n\nSample: `3 4 5` -> default `0 0 0 0`, parameterised `3 4 5 60`, copy `3 4 5 60`.\nConstraints: `0 <= dimension <= 10^5` (watch the overflow of the volume!)\n\nEdit `Solution.java`, then run:  `python3 judge.py class-box`\n",
    "solution": "import java.util.Scanner;\n\nclass Box {\n    private int length, breadth, height;\n\n    Box() {\n        // Write your code here\n    }\n\n    Box(int length, int breadth, int height) {\n        // Write your code here\n    }\n\n    Box(Box b1) {\n        // Write your code here\n    }\n\n    int getLength() {\n        return 0;\n    }\n\n    int getBreadth() {\n        return 0;\n    }\n\n    int getHeight() {\n        return 0;\n    }\n\n    long CalculateVolume() {\n        return 0;\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "OOP"
    ],
    "hints": [
      "Declare length, breadth, and height as private int variables.",
      "Volume can overflow 32-bit int with dimensions up to 10^5. Cast to (long) before multiplying.",
      "Implement the copy constructor by copying length, breadth, and height from the provided Box object."
    ],
    "sample_cases": [
      {
        "name": "default constructor",
        "input": "new Box()",
        "expected": "0 0 0 0"
      },
      {
        "name": "parameterised constructor (sample)",
        "input": "new Box(3, 4, 5)",
        "expected": "3 4 5 60"
      },
      {
        "name": "copy constructor (sample)",
        "input": "new Box(new Box(3, 4, 5))",
        "expected": "3 4 5 60"
      }
    ],
    "display_number": 3,
    "display_id": "03",
    "languages": [
      "Java"
    ],
    "path_id": "oop",
    "path_name": "OOP",
    "order_in_path": 1,
    "collection_ids": [
      "college-cuiet-lab",
      "exam-university",
      "exam-viva",
      "company-capgemini"
    ],
    "review_needed": false
  },
  "class-student": {
    "id": "class-student",
    "title": "Class Student",
    "summary": "Design `class Student`:",
    "readme": "# Class Student\n\n*Source: Practice-Test 8*\n\nDesign `class Student`:\n\n| Member | Behaviour |\n|---|---|\n| `Student(int studentId, String name, int[] marks)` | initialise (5 marks) |\n| `void printValues()` | line 1 id, line 2 name, line 3 the five marks space-separated |\n| `int calTotalMarks()` | sum of the five marks |\n| `int secondMaxMarks()` | second highest mark |\n\nSample: `14 / Deepak Singh / 57 85 45 86 95` -> total `368`, second highest `86`.\n\nEdit `Solution.java`, then run:  `python3 judge.py class-student`\n",
    "solution": "import java.util.*;\n\nclass Student {\n    private int studentId;\n    private String name;\n    private int[] marks;\n\n    // Constructor\n    public Student(int studentId, String name, int[] marks) {\n\n    }\n\n    public void printValues() {\n\n    }\n\n    public int calTotalMarks() {\n        return 0;\n    }\n\n    public int secondMaxMarks() {\n        return 0;\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "OOP",
      "Arrays"
    ],
    "hints": [
      "Save studentId, name, and marks (int array of 5 elements) into private instance fields in the constructor.",
      "printValues() prints studentId on line 1, name on line 2, and the 5 marks separated by spaces on line 3.",
      "secondMaxMarks() should determine the second highest value among the 5 marks."
    ],
    "sample_cases": [
      {
        "name": "printValues (sample)",
        "input": "14, \"Deepak Singh\", new int[]{57,85,45,86,95}).printValues(",
        "expected": "14\nDeepak Singh\n57 85 45 86 95\n"
      },
      {
        "name": "calTotalMarks (sample)",
        "input": "14, \"Deepak Singh\", new int[]{57,85,45,86,95}).calTotalMarks(",
        "expected": "368"
      },
      {
        "name": "secondMaxMarks (sample)",
        "input": "14, \"Deepak Singh\", new int[]{57,85,45,86,95}).secondMaxMarks(",
        "expected": "86"
      }
    ],
    "display_number": 4,
    "display_id": "04",
    "languages": [
      "Java"
    ],
    "path_id": "oop",
    "path_name": "OOP",
    "order_in_path": 2,
    "collection_ids": [
      "college-cuiet-lab",
      "exam-university",
      "exam-viva"
    ],
    "review_needed": false
  },
  "cloud-server-health": {
    "id": "cloud-server-health",
    "title": "Cloud Server Health Monitoring",
    "summary": "A server is **overloaded** when CPU utilisation is **>= 80**. Return the overloaded values in their original order.",
    "readme": "# Cloud Server Health Monitoring\n\n*Source: Practice-Test 11*\n\nA server is **overloaded** when CPU utilisation is **>= 80**. Return the overloaded values in their original order.\n\n`public static ArrayList<Integer> findOverloadedServers(ArrayList<Integer> cpuUsage)` in `class Main`\n\n`45 82 67 95 79 88 60` -> `82 95 88`\n\nEdit `Solution.java`, then run:  `python3 judge.py cloud-server-health`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static ArrayList<Integer>\n    findOverloadedServers(ArrayList<Integer> cpuUsage) {\n        // Write your code here\n        return new ArrayList<Integer>();\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Arrays",
      "Loops"
    ],
    "hints": [
      "Iterate through the cpuUsage ArrayList and select values where usage >= 80.",
      "Preserve the original order of the servers in the returned ArrayList."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "new ArrayList<>(List.of(45,82,67,95,79,88,60))",
        "expected": "List.of(82, 95, 88)"
      },
      {
        "name": "exactly 80 counts",
        "input": "new ArrayList<>(List.of(80,79,81))",
        "expected": "List.of(80, 81)"
      },
      {
        "name": "none overloaded",
        "input": "new ArrayList<>(List.of(10,20,79))",
        "expected": "List.of()"
      }
    ],
    "display_number": 5,
    "display_id": "05",
    "languages": [
      "Java"
    ],
    "path_id": "loops-functions",
    "path_name": "Loops & Functions",
    "order_in_path": 1,
    "collection_ids": [
      "college-placement",
      "company-amazon"
    ],
    "review_needed": true
  },
  "college-seats-reserved": {
    "id": "college-seats-reserved",
    "title": "College Seats Are Reserved",
    "summary": "`A[i]` is the age for which seat `i` is reserved, `B[i]` the age of applicant `i`. Return `true` if **every seat can be filled** (both arrays contain the same ages with the same frequencies, in any order).",
    "readme": "# College Seats Are Reserved\n\n*Source: Practice-Test 14*\n\n`A[i]` is the age for which seat `i` is reserved, `B[i]` the age of applicant `i`. Return `true` if **every seat can be filled** (both arrays contain the same ages with the same frequencies, in any order).\n\n`static boolean allSeatsFilled(int[] A, int[] B)` in `class Result`\n\n`[11,12,13,12,13]` / `[12,13,11,12,13]` -> YES, `[11,12,13]` / `[12,13,12]` -> NO\n\nConstraints: `1 <= N <= 10^5`, `1 <= A[i], B[i] <= 100`\n\nEdit `Solution.java`, then run:  `python3 judge.py college-seats-reserved`\n",
    "solution": "import java.io.*;\nimport java.math.*;\nimport java.util.*;\n\nclass Result {\n    // Return true or false based on the fact, whether all the seats will be filled\n    static boolean allSeatsFilled(int[] A, int[] B) {\n        // Write your code here\n        return false;\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "Arrays",
      "Loops"
    ],
    "hints": [
      "Sort both arrays A and B and verify whether they are identical at every index.",
      "Alternatively, tally the frequency of each age in A and B using a frequency map or array."
    ],
    "sample_cases": [
      {
        "name": "statement example 1",
        "input": "new int[]{11,12,13,12,13}, new int[]{12,13,11,12,13}",
        "expected": "true"
      },
      {
        "name": "statement example 2",
        "input": "new int[]{11,12,13}, new int[]{12,13,12}",
        "expected": "false"
      },
      {
        "name": "sample",
        "input": "new int[]{11,12,13}, new int[]{12,11,13}",
        "expected": "true"
      }
    ],
    "display_number": 6,
    "display_id": "06",
    "languages": [
      "Java"
    ],
    "path_id": "loops-functions",
    "path_name": "Loops & Functions",
    "order_in_path": 2,
    "collection_ids": [
      "college-placement",
      "exam-university"
    ],
    "review_needed": true
  },
  "compress-a-string": {
    "id": "compress-a-string",
    "title": "Compress a string",
    "summary": "Compress a string: every run of the same character longer than 1 is replaced by the character followed by the run length. Single characters stay unchanged.",
    "readme": "# Compress a string\n\n*Source: Practice-Test 5*\n\nCompress a string: every run of the same character longer than 1 is replaced by the character followed by the run length. Single characters stay unchanged.\n\n`public static String compressString(String str)` in `class Main`\n\n`aabbccdef` -> `a2b2c2def`, `abddddddd` -> `abd7`\n\nEdit `Solution.java`, then run:  `python3 judge.py compress-a-string`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static String compressString(String str) {\n        //write your code here\n        return \"\";\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Strings",
      "Loops"
    ],
    "hints": [
      "Traverse the string while counting consecutive occurrences of the current character.",
      "If a character occurs more than once, append the character followed by the count; otherwise, append just the character."
    ],
    "sample_cases": [
      {
        "name": "sample 1",
        "input": "\"aabbccdef\"",
        "expected": "a2b2c2def"
      },
      {
        "name": "sample 2",
        "input": "\"abddddddd\"",
        "expected": "abd7"
      },
      {
        "name": "no repeats",
        "input": "\"abc\"",
        "expected": "abc"
      }
    ],
    "display_number": 7,
    "display_id": "07",
    "languages": [
      "Java"
    ],
    "path_id": "strings",
    "path_name": "Strings",
    "order_in_path": 3,
    "collection_ids": [
      "company-tcs",
      "company-wipro",
      "college-placement"
    ],
    "review_needed": false
  },
  "count-pos-neg-even-odd": {
    "id": "count-pos-neg-even-odd",
    "title": "Count negative, positive, even and odd",
    "summary": "Given an array of 10 integers, print four lines: the count of **positive**, **negative**, **even** and **odd** elements (zero is even, neither positive nor negative).",
    "readme": "# Count negative, positive, even and odd\n\n*Source: Practice-Test 2*\n\nGiven an array of 10 integers, print four lines: the count of **positive**, **negative**, **even** and **odd** elements (zero is even, neither positive nor negative).\n\n`static void countAndPrint(int[] arr, int n)` in `class Result`\n\nInput `-3 10 20 -4 7 1 -2 3 4 5` -> `7`, `3`, `5`, `5` (one per line)\n\nEdit `Solution.java`, then run:  `python3 judge.py count-pos-neg-even-odd`\n",
    "solution": "import java.util.Scanner;\n\nclass Result {\n    static void countAndPrint(int[] arr, int n) {\n        // write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Loops",
      "Arrays"
    ],
    "hints": [
      "Zero (0) is an even number, but it is neither positive nor negative.",
      "Iterate through the array and track four counters: positive, negative, even, and odd.",
      "Print each counter on its own line in that specific order."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "new int[]{-3,10,20,-4,7,1,-2,3,4,5}, 10",
        "expected": "7\n3\n5\n5\n"
      },
      {
        "name": "with zeros",
        "input": "new int[]{0,0,1,-1,2,-2,3,-3,4,-4}, 10",
        "expected": "4\n4\n6\n4\n"
      },
      {
        "name": "all positive",
        "input": "new int[]{1,2,3,4,5,6,7,8,9,10}, 10",
        "expected": "10\n0\n5\n5\n"
      }
    ],
    "display_number": 8,
    "display_id": "08",
    "languages": [
      "Java"
    ],
    "path_id": "java-basics",
    "path_name": "Java Basics",
    "order_in_path": 1,
    "collection_ids": [
      "college-cuiet-lab",
      "exam-university",
      "company-wipro"
    ],
    "review_needed": false
  },
  "custom-exception-power": {
    "id": "custom-exception-power",
    "title": "Calculate positive power of a positive number",
    "summary": "Write `class CustomException extends Exception` with a private `String msg`, constructor `CustomException(String message)` and an overridden `String getMessage()` returning the stored message.",
    "readme": "# Calculate positive power of a positive number\n\n*Source: Practice-Test 15*\n\nWrite `class CustomException extends Exception` with a private `String msg`, constructor `CustomException(String message)` and an overridden `String getMessage()` returning the stored message.\nThen implement `static int power(int num, int exp) throws CustomException` in `class Main`:\n\n1. if `num` or `exp` is negative -> throw `CustomException(\"Negative numbers not allowed\")`\n2. else if both are zero -> throw `CustomException(\"Both can never be zero\")`\n3. otherwise return `num^exp`\n\n`-4 -5` -> `Negative numbers not allowed`, `2 2` -> `4`\n\nEdit `Solution.java`, then run:  `python3 judge.py custom-exception-power`\n",
    "solution": "import java.util.Scanner;\n// You can add other imports below\n\n//DO NOT CHANGE CLASS NAME\nclass CustomException extends Exception {\n    // Write Your Code Here\n\n}\n\n//DO NOT CHANGE CLASS NAME\nclass Main {\n\n    static int power(int num, int exp) throws CustomException {\n        // Write Your Code Here\n\n        return 0;\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "Functions",
      "OOP"
    ],
    "hints": [
      "Define a custom exception class extending Exception.",
      "If either n < 0 or p < 0, throw your custom exception with message 'Negative numbers not allowed'.",
      "Otherwise, calculate (long) Math.pow(n, p) and return as String."
    ],
    "sample_cases": [
      {
        "name": "2^2 = 4",
        "input": "2, 2",
        "expected": "4"
      },
      {
        "name": "both negative",
        "input": "-4, -5",
        "expected": "EX: Negative numbers not allowed"
      },
      {
        "name": "negative base",
        "input": "-2, 3",
        "expected": "EX: Negative numbers not allowed"
      }
    ],
    "display_number": 9,
    "display_id": "09",
    "languages": [
      "Java"
    ],
    "path_id": "oop",
    "path_name": "OOP",
    "order_in_path": 3,
    "collection_ids": [
      "exam-university",
      "exam-viva",
      "company-capgemini"
    ],
    "review_needed": false
  },
  "daily-loss-counter": {
    "id": "daily-loss-counter",
    "title": "The Daily Loss Counter",
    "summary": "Count the days with a **loss**, i.e. net performance strictly less than 0.",
    "readme": "# The Daily Loss Counter\n\n*Source: Practice-Test 5, 13*\n\nCount the days with a **loss**, i.e. net performance strictly less than 0.\n\n`public static int count(int[] a, int T)` in `class Solution`\n\n`1 2 3 -5` -> `1`\n\nConstraints: `1 <= T <= 1000`, `-10^6 <= a[i] <= 10^6`\n\nEdit `Solution.java`, then run:  `python3 judge.py daily-loss-counter`\n",
    "solution": "import java.util.*;\nimport java.io.*;\n\n// Do NOT change the class name\nclass Solution {\n    public static int count(int[] a, int T) {\n        // Write your code here\n        return 0;\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Loops",
      "Arrays"
    ],
    "hints": [
      "A loss day is strictly defined as an element where value < 0.",
      "Zero represents a break-even day and does not count as a loss."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "new int[]{1,2,3,-5}, 4",
        "expected": "1"
      },
      {
        "name": "zero is not a loss",
        "input": "new int[]{0,0,0}, 3",
        "expected": "0"
      },
      {
        "name": "all losses",
        "input": "new int[]{-1,-2,-3}, 3",
        "expected": "3"
      }
    ],
    "display_number": 10,
    "display_id": "10",
    "languages": [
      "Java"
    ],
    "path_id": "loops-functions",
    "path_name": "Loops & Functions",
    "order_in_path": 3,
    "collection_ids": [
      "company-tcs",
      "college-placement"
    ],
    "review_needed": false
  },
  "date-class": {
    "id": "date-class",
    "title": "Implement the Date class",
    "summary": "Implement `class Date` for a **non-leap year** (Feb always has 28 days). The year is not stored.",
    "readme": "# Implement the Date class\n\n*Source: Practice-Test 6*\n\nImplement `class Date` for a **non-leap year** (Feb always has 28 days). The year is not stored.\n\n| Member | Behaviour |\n|---|---|\n| `private int month, date` | 1-12 and day of month |\n| `Date()` | January 1st |\n| `Date(int m, int d)` | sets month and day |\n| `int daysInMonth()` | days in the current month (31 for Jan, 28 for Feb ...) |\n| `int getDay()` / `int getMonth()` | current values |\n| `void nextDay()` | +1 day, wraps to 1st of next month, Dec 31 -> Jan 1 |\n\nNo `main` needed.\n\nEdit `Solution.java`, then run:  `python3 judge.py date-class`\n",
    "solution": "class Date {\n    private int month;\n    private int date;\n\n    public Date() {\n\n    }\n\n    public Date(int month, int date) {\n\n    }\n\n    public int getMonth() {\n        return 0;\n    }\n\n    public int getDay() {\n        return 0;\n    }\n\n    public int daysInMonth() {\n        return 0;\n    }\n\n    public void nextDay() {\n\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "OOP",
      "Functions"
    ],
    "hints": [
      "Validate day, month, and year according to calendar rules and leap years if required.",
      "Format output with leading zeros where specified in the problem statement."
    ],
    "sample_cases": [
      {
        "name": "default constructor",
        "input": "{ Date d = new Date(",
        "expected": "1/1"
      },
      {
        "name": "sample: daysInMonth(3)",
        "input": "3, 25).daysInMonth(",
        "expected": "31"
      },
      {
        "name": "sample: getDay / getMonth",
        "input": "{ Date d = new Date(3, 25",
        "expected": "25 3"
      }
    ],
    "display_number": 11,
    "display_id": "11",
    "languages": [
      "Java"
    ],
    "path_id": "oop",
    "path_name": "OOP",
    "order_in_path": 4,
    "collection_ids": [
      "exam-university",
      "exam-viva",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "employee": {
    "id": "employee",
    "title": "Employee",
    "summary": "Track six months of salaries for an employee.",
    "readme": "# Employee\n\n*Source: Practice-Test 7*\n\nTrack six months of salaries for an employee.\n\n| Method | Behaviour |\n|---|---|\n| `void getValues(int id, String name, int[] salary)` | store the data |\n| `void printValues()` | print id, name (may contain spaces), the six salaries space-separated - 3 lines |\n| `int calTotalSalary()` | sum of the six salaries |\n| `int maxSalary()` | month number (1-6) of the highest salary |\n\nSample: `3234 / Nitin Kumar / 12313 12001 10333 14923 15783 10010` -> total `75363`, max in month `5`.\n\nEdit `Solution.java`, then run:  `python3 judge.py employee`\n",
    "solution": "import java.util.Scanner;\n\nclass Employee {\n    private int e_Id;\n    private String name;\n    private int[] salary = new int[6];\n\n    public void getValues(int id, String name, int[] salary) {\n\n    }\n\n    public void printValues() {}\n\n    public int calTotalSalary() {\n        return 0;\n    }\n\n    public int maxSalary() {\n        return 0;\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "OOP",
      "Arrays"
    ],
    "hints": [
      "Store the employee ID, name, and 6 months of salary in private fields.",
      "totalSalary() sums up the salary across all 6 months.",
      "maxSalaryMonth() returns the 1-based index (1 to 6) of the month with the highest salary."
    ],
    "sample_cases": [
      {
        "name": "printValues (sample)",
        "input": "{ Employee e = new Employee(",
        "expected": "3234\nNitin Kumar\n12313 12001 10333 14923 15783 10010\n"
      },
      {
        "name": "calTotalSalary (sample)",
        "input": "{ Employee e = new Employee(",
        "expected": "75363"
      },
      {
        "name": "maxSalary (sample) -> month 5",
        "input": "{ Employee e = new Employee(",
        "expected": "5"
      }
    ],
    "display_number": 12,
    "display_id": "12",
    "languages": [
      "Java"
    ],
    "path_id": "oop",
    "path_name": "OOP",
    "order_in_path": 5,
    "collection_ids": [
      "college-cuiet-lab",
      "exam-university",
      "company-infosys"
    ],
    "review_needed": false
  },
  "exam-topper": {
    "id": "exam-topper",
    "title": "Exam Topper",
    "summary": "Given the marks of `N` students, return the **maximum** marks scored by any student.",
    "readme": "# Exam Topper\n\n*Source: Practice-Test 1, 12*\n\nGiven the marks of `N` students, return the **maximum** marks scored by any student.\n\n`static int maxMarks(int[] marks, int N)` in `class Result`\n\nConstraints: `1 <= N <= 10^5`, `-1000 <= marks[i] <= 1000`\n\n| Input | Output |\n|---|---|\n| `20 30 93 71 18 82 66` | `93` |\n| `33 45 67 33 67` | `67` |\n\nEdit `Solution.java`, then run:  `python3 judge.py exam-topper`\n",
    "solution": "import java.util.*;\n\nclass Result {\n    static int maxMarks(int[] marks, int N) {\n        // Write Your Code here\n        return 0;\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Arrays",
      "Searching"
    ],
    "hints": [
      "Scan the marks array to find the maximum value.",
      "Return the 1-based position or highest mark as requested in the problem description."
    ],
    "sample_cases": [
      {
        "name": "sample 1",
        "input": "new int[]{20,30,93,71,18,82,66}, 7",
        "expected": "93"
      },
      {
        "name": "sample 2 (max repeated)",
        "input": "new int[]{33,45,67,33,67}, 5",
        "expected": "67"
      },
      {
        "name": "single element",
        "input": "new int[]{-5}, 1",
        "expected": "-5"
      }
    ],
    "display_number": 13,
    "display_id": "13",
    "languages": [
      "Java"
    ],
    "path_id": "sorting-searching",
    "path_name": "Sorting & Searching",
    "order_in_path": 1,
    "collection_ids": [
      "college-cuiet-lab",
      "company-tcs"
    ],
    "review_needed": false
  },
  "find-the-longest-word": {
    "id": "find-the-longest-word",
    "title": "Find the Longest Word",
    "summary": "Return the longest word in a sentence (letters and single spaces only, no leading/trailing spaces).",
    "readme": "# Find the Longest Word\n\n*Source: Practice-Test 7*\n\nReturn the longest word in a sentence (letters and single spaces only, no leading/trailing spaces).\n\n`public static String findLongestWord(String input)` in `class Main`\n\n`I love programming` -> `programming`\n\nConstraints: sentence length <= 10^5 (tests have a unique longest word)\n\nEdit `Solution.java`, then run:  `python3 judge.py find-the-longest-word`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static String findLongestWord(String input) {\n        // Write Your Code Here\n        return \"\";\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Strings",
      "Searching"
    ],
    "hints": [
      "Split the sentence into words using spaces as delimiters.",
      "Track the word with the maximum length and return it."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "\"I love programming\"",
        "expected": "programming"
      },
      {
        "name": "single word",
        "input": "\"hello\"",
        "expected": "hello"
      },
      {
        "name": "longest in the middle",
        "input": "\"a bb ccc dd e\"",
        "expected": "ccc"
      }
    ],
    "display_number": 14,
    "display_id": "14",
    "languages": [
      "Java"
    ],
    "path_id": "strings",
    "path_name": "Strings",
    "order_in_path": 4,
    "collection_ids": [
      "company-wipro",
      "college-placement"
    ],
    "review_needed": false
  },
  "layered-pyramid-3": {
    "id": "layered-pyramid-3",
    "title": "Layered Calibration Code Pyramid - 3",
    "summary": "Read `n`. Row `i` (1..n) prints `n-i` stars followed by `1..i` (no spaces).",
    "readme": "# Layered Calibration Code Pyramid - 3\n\n*Source: Practice-Test 5*\n\nRead `n`. Row `i` (1..n) prints `n-i` stars followed by `1..i` (no spaces).\n\nInput `5` ->\n```\n****1\n***12\n**123\n*1234\n12345\n```\n\nEdit `Solution.java`, then run:  `python3 judge.py layered-pyramid-3`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Loops"
    ],
    "hints": [
      "Observe the outer loop for rows (1 to n) and inner loop for spaces and numbers.",
      "Ensure spacing aligns with the pyramid format."
    ],
    "sample_cases": [
      {
        "name": "n = 5",
        "input": "n = 5",
        "expected": "\"5\\n\", exp(5), Test::go"
      },
      {
        "name": "n = 3",
        "input": "n = 3",
        "expected": "\"3\\n\", exp(3), Test::go"
      },
      {
        "name": "n = 1",
        "input": "n = 1",
        "expected": "\"1\\n\", exp(1), Test::go"
      }
    ],
    "display_number": 15,
    "display_id": "15",
    "languages": [
      "Java"
    ],
    "path_id": "loops-functions",
    "path_name": "Loops & Functions",
    "order_in_path": 4,
    "collection_ids": [
      "college-cuiet-lab",
      "company-tcs"
    ],
    "review_needed": false
  },
  "library-book-inventory": {
    "id": "library-book-inventory",
    "title": "Library Book Inventory Management",
    "summary": "Add each newly arrived book id to the inventory **only if it is not already present** (duplicates inside `newBooks` also count). Return the updated `ArrayList`.",
    "readme": "# Library Book Inventory Management\n\n*Source: Practice-Test 15*\n\nAdd each newly arrived book id to the inventory **only if it is not already present** (duplicates inside `newBooks` also count). Return the updated `ArrayList`.\n\n`public static ArrayList<Integer> updateInventory(ArrayList<Integer> books, int[] newBooks)` in `class Main`\n\n`101 102 103 104` + `104 105 106 102 107` -> `101 102 103 104 105 106 107`\n\nEdit `Solution.java`, then run:  `python3 judge.py library-book-inventory`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static ArrayList<Integer>\n    updateInventory(ArrayList<Integer> books, int[] newBooks) {\n        //write your code here\n        return null;\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "OOP",
      "Arrays"
    ],
    "hints": [
      "Manage inventory operations using appropriate Java Collections (e.g., HashMap or ArrayList).",
      "Handle case sensitivity and missing book lookups gracefully."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "al(101,102,103,104), new int[]{104,105,106,102,107}",
        "expected": "List.of(101,102,103,104,105,106,107)"
      },
      {
        "name": "statement example",
        "input": "al(101,102,103), new int[]{102,104,105,101,106}",
        "expected": "List.of(101,102,103,104,105,106)"
      },
      {
        "name": "all already present",
        "input": "al(1,2,3), new int[]{3,2,1}",
        "expected": "List.of(1,2,3)"
      }
    ],
    "display_number": 16,
    "display_id": "16",
    "languages": [
      "Java"
    ],
    "path_id": "oop",
    "path_name": "OOP",
    "order_in_path": 6,
    "collection_ids": [
      "college-cuiet-lab",
      "exam-university"
    ],
    "review_needed": false
  },
  "lowercase-to-uppercase": {
    "id": "lowercase-to-uppercase",
    "title": "Convert lower case to upper case",
    "summary": "Read a string of lowercase letters (a-z, length 1..1000) and print it in uppercase.",
    "readme": "# Convert lower case to upper case\n\n*Source: Practice-Test 4*\n\nRead a string of lowercase letters (a-z, length 1..1000) and print it in uppercase.\n\n`codequotient` -> `CODEQUOTIENT`\n\nEdit `Solution.java`, then run:  `python3 judge.py lowercase-to-uppercase`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // Write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Strings",
      "Functions"
    ],
    "hints": [
      "Convert ASCII values by subtracting 32 or using Character.toUpperCase(c).",
      "Only alter lowercase letters ('a' through 'z'); leave digits and punctuation intact."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "sample",
        "expected": "\"codequotient\\n\", \"CODEQUOTIENT\\n\", Test::go"
      },
      {
        "name": "single letter",
        "input": "single letter",
        "expected": "\"q\\n\", \"Q\\n\", Test::go"
      },
      {
        "name": "whole alphabet",
        "input": "whole alphabet",
        "expected": "\"abcdefghijklmnopqrstuvwxyz\\n\", \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\\n\", Test::go"
      }
    ],
    "display_number": 17,
    "display_id": "17",
    "languages": [
      "Java"
    ],
    "path_id": "java-basics",
    "path_name": "Java Basics",
    "order_in_path": 2,
    "collection_ids": [
      "company-wipro",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "main-diagonal-sum": {
    "id": "main-diagonal-sum",
    "title": "Find sum of main diagonal of matrix",
    "summary": "Return the sum of the main diagonal of an `m x m` matrix.",
    "readme": "# Find sum of main diagonal of matrix\n\n*Source: Practice-Test 9*\n\nReturn the sum of the main diagonal of an `m x m` matrix.\n\n`public static int mainDiagonalSum(int[][] matrix, int m)` in `class Main`\n\n`[[1,2,3],[4,5,6],[7,8,9]]` -> `1+5+9 = 15`\n\nEdit `Solution.java`, then run:  `python3 judge.py main-diagonal-sum`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static int mainDiagonalSum(int[][] matrix, int m) {\n        //write your code here\n        return 0;\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Arrays",
      "Loops"
    ],
    "hints": [
      "The main diagonal contains elements where row index equals column index (matrix[i][i]).",
      "A single loop from i = 0 to n-1 is sufficient to compute the sum in O(n) time."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "new int[][]{{1,2,3},{4,5,6},{7,8,9}}, 3",
        "expected": "15"
      },
      {
        "name": "1x1",
        "input": "new int[][]{{-4}}, 1",
        "expected": "-4"
      },
      {
        "name": "negatives",
        "input": "new int[][]{{-1,2,3},{4,-5,6},{7,8,-9}}, 3",
        "expected": "-15"
      }
    ],
    "display_number": 18,
    "display_id": "18",
    "languages": [
      "Java"
    ],
    "path_id": "sorting-searching",
    "path_name": "Sorting & Searching",
    "order_in_path": 2,
    "collection_ids": [
      "exam-university",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "matrix-multiplication": {
    "id": "matrix-multiplication",
    "title": "Matrix Multiplication",
    "summary": "Multiply `A (R1 x C1)` by `B (C1 x C2)` and return the `R1 x C2` result.",
    "readme": "# Matrix Multiplication\n\n*Source: Practice-Test 7*\n\nMultiply `A (R1 x C1)` by `B (C1 x C2)` and return the `R1 x C2` result.\n\n`public static int[][] multiply(int[][] A, int[][] B, int R1, int C1, int C2)` in `class Main`\n\n`[[1,2,3],[4,5,6]] x [[2,3],[1,2],[2,1]]` -> `[[10,10],[25,28]]`\n\nConstraints: `-1000 <= elements <= 1000`\n\nEdit `Solution.java`, then run:  `python3 judge.py matrix-multiplication`\n",
    "solution": "class Main {\n    public static int[][] multiply(int[][] A, int[][] B, int R1, int C1, int C2) {\n        // write your code here\n        return null;\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "Arrays",
      "Loops"
    ],
    "hints": [
      "Columns of matrix A must equal rows of matrix B.",
      "Use three nested loops: result[i][j] += A[i][k] * B[k][j]."
    ],
    "sample_cases": [
      {
        "name": "sample test 1",
        "input": "new int[][]{{1,2,3},{4,5,6}}, new int[][]{{2,3},{1,2},{2,1}}, 2, 3, 2",
        "expected": "new int[][]{{10,10},{25,28}}"
      },
      {
        "name": "sample test 2",
        "input": "new int[][]{{12,4},{7,6}}, new int[][]{{2,4,6},{3,5,7}}, 2, 2, 3",
        "expected": "new int[][]{{36,68,100},{32,58,84}}"
      },
      {
        "name": "1x1",
        "input": "new int[][]{{2}}, new int[][]{{-3}}, 1, 1, 1",
        "expected": "new int[][]{{-6}}"
      }
    ],
    "display_number": 19,
    "display_id": "19",
    "languages": [
      "Java"
    ],
    "path_id": "sorting-searching",
    "path_name": "Sorting & Searching",
    "order_in_path": 3,
    "collection_ids": [
      "exam-university",
      "exam-gate",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "matrix-row-and-column-sum": {
    "id": "matrix-row-and-column-sum",
    "title": "Sum of elements of matrix",
    "summary": "Read `rows`, `cols`, the matrix, a row index `r` and a column index `c` (0-based). Print **sum(row r) + sum(column c)**",
    "readme": "# Sum of elements of matrix\n\n*Source: Practice-Test 6*\n\nRead `rows`, `cols`, the matrix, a row index `r` and a column index `c` (0-based). Print **sum(row r) + sum(column c)**\n(the element at `[r][c]` is counted twice).\n\nInput\n```\n2\n3\n1 2 3\n4 5 6\n0\n0\n```\nOutput `11`  (row0 = 6, col0 = 5)\n\nEdit `Solution.java`, then run:  `python3 judge.py matrix-row-and-column-sum`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // Write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Arrays",
      "Loops"
    ],
    "hints": [
      "Compute row sums by iterating columns for each row.",
      "Compute column sums by iterating rows for each column."
    ],
    "sample_cases": [
      {
        "name": "sample 2",
        "input": "sample 2",
        "expected": "\"2\\n3\\n1 2 3\\n4 5 6\\n0\\n0\\n\", \"11\\n\", Test::go"
      },
      {
        "name": "3x3, row 1 + column 2",
        "input": "3x3, row 1 + column 2",
        "expected": "\"3\\n3\\n1 2 3\\n2 2 2\\n4 5 3\\n1\\n2\\n\", \"14\\n\", Test::go"
      },
      {
        "name": "1x1",
        "input": "1x1",
        "expected": "\"1\\n1\\n5\\n0\\n0\\n\", \"10\\n\", Test::go"
      }
    ],
    "display_number": 20,
    "display_id": "20",
    "languages": [
      "Java"
    ],
    "path_id": "sorting-searching",
    "path_name": "Sorting & Searching",
    "order_in_path": 4,
    "collection_ids": [
      "exam-university",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "mycalculator-exception": {
    "id": "mycalculator-exception",
    "title": "MyCalculator Exception",
    "summary": "`class MyException extends Exception` (with an `int code`) is provided. Implement `static void power(int n, int p)` in `class Main` that **throws, catches (inside `power`) and prints the error code**:",
    "readme": "# MyCalculator Exception\n\n*Source: Practice-Test 12*\n\n`class MyException extends Exception` (with an `int code`) is provided. Implement `static void power(int n, int p)` in `class Main` that **throws, catches (inside `power`) and prints the error code**:\n\n1. if `n` or `p` is negative -> throw `MyException(-1)` -> print `-1`\n2. else if both are `0` -> throw `MyException(-2)` -> print `-2`\n3. otherwise print `n^p`\n\nInput `2 3` `-3 2` `0 0` `5 0` `0 5` -> `8 -1 -2 1 0` (one per line)\n\nEdit `Solution.java`, then run:  `python3 judge.py mycalculator-exception`\n",
    "solution": "import java.util.Scanner;\n\nclass MyException extends Exception {\n    int code;\n\n    MyException(int code) {\n        this.code = code;\n    }\n}\n\nclass Main {\n    static void power(int n, int p) {\n        //write your code here\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "Functions",
      "OOP"
    ],
    "hints": [
      "If either n or p is negative, throw an Exception: 'n or p should not be negative.'",
      "If both n and p are zero, throw an Exception: 'n and p should not be zero.'",
      "Otherwise compute and return (long) Math.pow(n, p)."
    ],
    "sample_cases": [
      {
        "name": "2^3 = 8",
        "input": "2, 3",
        "expected": "8\n"
      },
      {
        "name": "negative n",
        "input": "-3, 2",
        "expected": "-1\n"
      },
      {
        "name": "both zero",
        "input": "0, 0",
        "expected": "-2\n"
      }
    ],
    "display_number": 21,
    "display_id": "21",
    "languages": [
      "Java"
    ],
    "path_id": "oop",
    "path_name": "OOP",
    "order_in_path": 7,
    "collection_ids": [
      "exam-viva",
      "exam-university",
      "company-infosys"
    ],
    "review_needed": false
  },
  "perfect-string": {
    "id": "perfect-string",
    "title": "Perfect String",
    "summary": "A string made only of `a`, `b`, `x`, `y` is **perfect** if the number of `a`+`b` characters is **odd** and the number of `x`+`y` characters is **even**.",
    "readme": "# Perfect String\n\n*Source: Practice-Test 8*\n\nA string made only of `a`, `b`, `x`, `y` is **perfect** if the number of `a`+`b` characters is **odd** and the number of `x`+`y` characters is **even**.\n\n`public static boolean isPerfect(String str)` in `class Result`\n\n`xaxbyyb` (3 / 4) -> YES, `aabbxxyy` (4 / 4) -> NO, `abaabxy` (5 / 2) -> YES, `yyxaby` (2 / 4) -> NO\n\nEdit `Solution.java`, then run:  `python3 judge.py perfect-string`\n",
    "solution": "import java.io.*;\nimport java.util.*;\n\nclass Result {\n    /*\n     * Complete the 'isPerfect' function below.\n     * @params str -> a string that is to be tested\n     * @return boolean value, whether the given string is perfect or not.\n     */\n    public static boolean isPerfect(String str) {\n        // Write your code here\n        return false;\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Strings",
      "Searching"
    ],
    "hints": [
      "A string is perfect if all alphabetic letters appear at least once (pangram) or meet the problem's condition.",
      "Use a boolean array of size 26 or a Set<Character> to track seen letters."
    ],
    "sample_cases": [
      {
        "name": "sample 1: xaxbyyb",
        "input": "\"xaxbyyb\"",
        "expected": "true"
      },
      {
        "name": "sample 2: aabbxxyy",
        "input": "\"aabbxxyy\"",
        "expected": "false"
      },
      {
        "name": "sample 3: abaabxy",
        "input": "\"abaabxy\"",
        "expected": "true"
      }
    ],
    "display_number": 22,
    "display_id": "22",
    "languages": [
      "Java"
    ],
    "path_id": "strings",
    "path_name": "Strings",
    "order_in_path": 5,
    "collection_ids": [
      "company-tcs",
      "college-placement"
    ],
    "review_needed": false
  },
  "pyramid-13": {
    "id": "pyramid-13",
    "title": "Pyramid - 13",
    "summary": "Read `n` and print `n` rows: row 1 has `n` stars, each next row has one star fewer (last row has 1 star).",
    "readme": "# Pyramid - 13\n\n*Source: Practice-Test 1*\n\nRead `n` and print `n` rows: row 1 has `n` stars, each next row has one star fewer (last row has 1 star).\n\nConstraints: `1 <= n <= 50`\n\nInput `5` ->\n```\n*****\n****\n***\n**\n*\n```\n\nEdit `Solution.java`, then run:  `python3 judge.py pyramid-13`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Loops"
    ],
    "hints": [
      "Determine the row count and number of stars/numbers per line.",
      "Check prefix spaces carefully for row alignment."
    ],
    "sample_cases": [
      {
        "name": "n = 5",
        "input": "n = 5",
        "expected": "\"5\\n\", exp(5), Test::go"
      },
      {
        "name": "n = 1",
        "input": "n = 1",
        "expected": "\"1\\n\", exp(1), Test::go"
      },
      {
        "name": "n = 3",
        "input": "n = 3",
        "expected": "\"3\\n\", exp(3), Test::go"
      }
    ],
    "display_number": 23,
    "display_id": "23",
    "languages": [
      "Java"
    ],
    "path_id": "loops-functions",
    "path_name": "Loops & Functions",
    "order_in_path": 5,
    "collection_ids": [
      "company-wipro",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "pyramid-4": {
    "id": "pyramid-4",
    "title": "Pyramid - 4",
    "summary": "Read `n`. Row `i` (1..n) prints `n-i` stars followed by the numbers `i, i-1, ... 1` (no spaces).",
    "readme": "# Pyramid - 4\n\n*Source: Practice-Test 2*\n\nRead `n`. Row `i` (1..n) prints `n-i` stars followed by the numbers `i, i-1, ... 1` (no spaces).\n\nInput `5` ->\n```\n****1\n***21\n**321\n*4321\n54321\n```\n\nEdit `Solution.java`, then run:  `python3 judge.py pyramid-4`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Loops"
    ],
    "hints": [
      "Print spaces descending and characters/numbers ascending per row.",
      "Ensure each line terminates with a newline."
    ],
    "sample_cases": [
      {
        "name": "n = 5",
        "input": "n = 5",
        "expected": "\"5\\n\", exp(5), Test::go"
      },
      {
        "name": "n = 3",
        "input": "n = 3",
        "expected": "\"3\\n\", exp(3), Test::go"
      },
      {
        "name": "n = 1",
        "input": "n = 1",
        "expected": "\"1\\n\", exp(1), Test::go"
      }
    ],
    "display_number": 24,
    "display_id": "24",
    "languages": [
      "Java"
    ],
    "path_id": "loops-functions",
    "path_name": "Loops & Functions",
    "order_in_path": 6,
    "collection_ids": [
      "company-tcs",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "pyramid-9": {
    "id": "pyramid-9",
    "title": "Pyramid - 9",
    "summary": "Day 1 has items `1..n`. Each following day the last item is removed. Print the row for every day.",
    "readme": "# Pyramid - 9\n\n*Source: Practice-Test 3*\n\nDay 1 has items `1..n`. Each following day the last item is removed. Print the row for every day.\n\nInput `3` ->\n```\n123\n12\n1\n```\n\nEdit `Solution.java`, then run:  `python3 judge.py pyramid-9`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Loops"
    ],
    "hints": [
      "Inspect the symmetry of the pattern.",
      "Handle odd and even increments according to the sample specification."
    ],
    "sample_cases": [
      {
        "name": "n = 3",
        "input": "n = 3",
        "expected": "\"3\\n\", exp(3), Test::go"
      },
      {
        "name": "n = 1",
        "input": "n = 1",
        "expected": "\"1\\n\", exp(1), Test::go"
      },
      {
        "name": "n = 5",
        "input": "n = 5",
        "expected": "\"5\\n\", exp(5), Test::go"
      }
    ],
    "display_number": 25,
    "display_id": "25",
    "languages": [
      "Java"
    ],
    "path_id": "loops-functions",
    "path_name": "Loops & Functions",
    "order_in_path": 7,
    "collection_ids": [
      "company-tcs",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "quality-check": {
    "id": "quality-check",
    "title": "Quality Check (even / odd count)",
    "summary": "Given `T` integers, print the count of **even** and **odd** elements on one line separated by a space (even first).",
    "readme": "# Quality Check (even / odd count)\n\n*Source: Practice-Test 4, 11*\n\nGiven `T` integers, print the count of **even** and **odd** elements on one line separated by a space (even first).\n\n`static void count(int[] a, int T)` in `class Solution`\n\n`1 3 5 8` -> `1 3`\n\nConstraints: `1 <= T <= 100`, `1 <= a[i] <= 10^5`\n\nEdit `Solution.java`, then run:  `python3 judge.py quality-check`\n",
    "solution": "import java.util.*;\n\nclass Solution {\n    static void count(int[] a, int T) {\n        //write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Arrays",
      "Searching"
    ],
    "hints": [
      "Check each element against the minimum threshold.",
      "Count or filter elements that pass quality inspection."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "new int[]{1,3,5,8}, 4",
        "expected": "1 3\n"
      },
      {
        "name": "all even",
        "input": "new int[]{2,4,6}, 3",
        "expected": "3 0\n"
      },
      {
        "name": "all odd",
        "input": "new int[]{1,1,1,1,1}, 5",
        "expected": "0 5\n"
      }
    ],
    "display_number": 26,
    "display_id": "26",
    "languages": [
      "Java"
    ],
    "path_id": "sorting-searching",
    "path_name": "Sorting & Searching",
    "order_in_path": 5,
    "collection_ids": [
      "company-infosys",
      "college-placement"
    ],
    "review_needed": false
  },
  "save-bandwidth-compression": {
    "id": "save-bandwidth-compression",
    "title": "Save Bandwidth Using Compression",
    "summary": "Compress a text message: each **consecutive run** of a character longer than 1 becomes `char + count`.",
    "readme": "# Save Bandwidth Using Compression\n\n*Source: Practice-Test 6*\n\nCompress a text message: each **consecutive run** of a character longer than 1 becomes `char + count`.\n\n`static String compressMsg(String textMsg)` in `class Result`\n\n`ggkkgdddgggg` -> `g2k2gd3g4`, `abddddddd` -> `abd7`\n\nEdit `Solution.java`, then run:  `python3 judge.py save-bandwidth-compression`\n",
    "solution": "import java.util.*;\n\nclass Result {\n    // return the compressed string\n    static String compressMsg(String textMsg) {\n        // Write your code here\n        return \"\";\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "Strings",
      "Loops"
    ],
    "hints": [
      "Compress repeated sequences to reduce data size.",
      "Handle single characters without unnecessary count suffixes."
    ],
    "sample_cases": [
      {
        "name": "sample 1",
        "input": "\"aabbccdef\"",
        "expected": "a2b2c2def"
      },
      {
        "name": "sample 2",
        "input": "\"abddddddd\"",
        "expected": "abd7"
      },
      {
        "name": "no repeats",
        "input": "\"abc\"",
        "expected": "abc"
      }
    ],
    "display_number": 27,
    "display_id": "27",
    "languages": [
      "Java"
    ],
    "path_id": "strings",
    "path_name": "Strings",
    "order_in_path": 6,
    "collection_ids": [
      "company-amazon",
      "college-placement"
    ],
    "review_needed": false
  },
  "search-an-element": {
    "id": "search-an-element",
    "title": "Search an element",
    "summary": "An array has a fixed size of 7. Return the **number of times** `ele` occurs in it, or `-1` if it is not present.",
    "readme": "# Search an element\n\n*Source: Practice-Test 3, 15*\n\nAn array has a fixed size of 7. Return the **number of times** `ele` occurs in it, or `-1` if it is not present.\n\n`static int SearchElement(int[] arr, int ele)` in `class Search`\n\nArray `3 10 20 4 7 4 5`: `4` -> `2`, `5` -> `1`, `6` -> `-1`\n\nEdit `Solution.java`, then run:  `python3 judge.py search-an-element`\n",
    "solution": "import java.util.Scanner;\n\nclass Search {\n    static int SearchElement(int[] arr, int ele) {\n        //write your code here\n        return 0;\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Searching",
      "Arrays"
    ],
    "hints": [
      "Traverse the array linearly and compare each element to the target key.",
      "Return the 0-based index if found, or -1 if the key is not present."
    ],
    "sample_cases": [
      {
        "name": "appears twice",
        "input": "a, 4",
        "expected": "2"
      },
      {
        "name": "appears once",
        "input": "a, 5",
        "expected": "1"
      },
      {
        "name": "not present",
        "input": "a, 6",
        "expected": "-1"
      }
    ],
    "display_number": 28,
    "display_id": "28",
    "languages": [
      "Java"
    ],
    "path_id": "sorting-searching",
    "path_name": "Sorting & Searching",
    "order_in_path": 6,
    "collection_ids": [
      "exam-gate",
      "company-tcs",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "separate-even-odd": {
    "id": "separate-even-odd",
    "title": "Put even and odd elements in 2 separate arrays",
    "summary": "Split the array into an array of even elements and an array of odd elements (keep the original order), then **print** the even elements on the first line and the odd elements on the second line, space-separated. Do not read input.",
    "readme": "# Put even and odd elements in 2 separate arrays\n\n*Source: Practice-Test 14*\n\nSplit the array into an array of even elements and an array of odd elements (keep the original order), then **print** the even elements on the first line and the odd elements on the second line, space-separated. Do not read input.\n\n`static void separate(int a[], int n)` in `class Main`\n\n`1 3 5 8` -> `8` / `1 3 5`\n\nConstraints: `1 <= n <= 100`, `-10^9 <= a[i] <= 10^9` (negative odd numbers exist!)\n\nEdit `Solution.java`, then run:  `python3 judge.py separate-even-odd`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    // This function separates the elements of the array into even and odd.\n    // It prints all even elements in the first line and odd elements in the second line.\n    static void separate(int a[], int n) {\n        // write your code here.\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Arrays",
      "Loops"
    ],
    "hints": [
      "Create two sub-lists or separate passes for even numbers and odd numbers.",
      "Preserve the relative ordering of elements if stable ordering is required."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "new int[]{1,3,5,8}, 4",
        "expected": "8\n1 3 5\n"
      },
      {
        "name": "order is preserved",
        "input": "new int[]{2,1,4,3}, 4",
        "expected": "2 4\n1 3\n"
      },
      {
        "name": "negative numbers and zero",
        "input": "new int[]{10,-3,7,-8,0,5}, 6",
        "expected": "10 -8 0\n-3 7 5\n"
      }
    ],
    "display_number": 29,
    "display_id": "29",
    "languages": [
      "Java"
    ],
    "path_id": "java-basics",
    "path_name": "Java Basics",
    "order_in_path": 3,
    "collection_ids": [
      "company-wipro",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "sequential-id-pyramid-7": {
    "id": "sequential-id-pyramid-7",
    "title": "Sequential ID Pyramid - 7",
    "summary": "Read `n`. Row `i` has `i` consecutive ids, continuing the counter from the previous row. Separate numbers in a row with a single space.",
    "readme": "# Sequential ID Pyramid - 7\n\n*Source: Practice-Test 4*\n\nRead `n`. Row `i` has `i` consecutive ids, continuing the counter from the previous row. Separate numbers in a row with a single space.\n\nInput `3` ->\n```\n1\n2 3\n4 5 6\n```\nConstraints: `1 <= n <= 50`\n\nEdit `Solution.java`, then run:  `python3 judge.py sequential-id-pyramid-7`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Loops"
    ],
    "hints": [
      "Track a running sequence counter across rows.",
      "Print the counter formatted with required spaces."
    ],
    "sample_cases": [
      {
        "name": "n = 3",
        "input": "n = 3",
        "expected": "\"3\\n\", \"1\\n2 3\\n4 5 6\\n\", Test::go"
      },
      {
        "name": "n = 1",
        "input": "n = 1",
        "expected": "\"1\\n\", \"1\\n\", Test::go"
      },
      {
        "name": "n = 4",
        "input": "n = 4",
        "expected": "\"4\\n\", \"1\\n2 3\\n4 5 6\\n7 8 9 10\\n\", Test::go"
      }
    ],
    "display_number": 30,
    "display_id": "30",
    "languages": [
      "Java"
    ],
    "path_id": "loops-functions",
    "path_name": "Loops & Functions",
    "order_in_path": 8,
    "collection_ids": [
      "company-tcs",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "stock-price-trend": {
    "id": "stock-price-trend",
    "title": "Stock Trading - Price Trend Analyzer",
    "summary": "Return a **new** `LinkedList` with every price that is **strictly greater** than the previous trading session's price (the first price is ignored). Keep the original order, do not modify the input, empty list if none.",
    "readme": "# Stock Trading - Price Trend Analyzer\n\n*Source: Practice-Test 13*\n\nReturn a **new** `LinkedList` with every price that is **strictly greater** than the previous trading session's price (the first price is ignored). Keep the original order, do not modify the input, empty list if none.\n\n`public static LinkedList<Integer> findIncreasingPrices(LinkedList<Integer> prices)` in `class Main`\n\n`500 520 510 550 550 580 560` -> `520 550 580`\n\nEdit `Solution.java`, then run:  `python3 judge.py stock-price-trend`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static LinkedList<Integer>\n    findIncreasingPrices(LinkedList<Integer> prices) {\n\n        // Write your code here\n        return null;\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "Arrays",
      "Searching"
    ],
    "hints": [
      "Compare adjacent price points: price[i] > price[i-1] indicates an upward trend.",
      "Use a Deque or List to track running windows if required."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "ll(500,520,510,550,550,580,560)",
        "expected": "List.of(520, 550, 580)"
      },
      {
        "name": "strictly decreasing -> empty",
        "input": "ll(50,40,30,20)",
        "expected": "List.of()"
      },
      {
        "name": "single price -> empty",
        "input": "ll(100)",
        "expected": "List.of()"
      }
    ],
    "display_number": 31,
    "display_id": "31",
    "languages": [
      "Java"
    ],
    "path_id": "sorting-searching",
    "path_name": "Sorting & Searching",
    "order_in_path": 7,
    "collection_ids": [
      "company-amazon",
      "company-infosys"
    ],
    "review_needed": false
  },
  "strings-are-anagram": {
    "id": "strings-are-anagram",
    "title": "Strings are anagram or not",
    "summary": "Two strings are **anagrams** if they contain the same characters (case matters) with the same frequencies. Return `1` if anagram, else `0`.",
    "readme": "# Strings are anagram or not\n\n*Source: Practice-Test 9*\n\nTwo strings are **anagrams** if they contain the same characters (case matters) with the same frequencies. Return `1` if anagram, else `0`.\n\n`static int isAnagram(String str1, String str2)` in `class Main`\n\n`act`/`cat` -> 1, `CodeQuotient`/`QuotientCode` -> 1, `Hello`/`Hillo` -> 0\n\nEdit `Solution.java`, then run:  `python3 judge.py strings-are-anagram`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    static int isAnagram(String str1, String str2) {\n        // Write your code here\n        return 0;\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Strings",
      "Sorting"
    ],
    "hints": [
      "Two strings are anagrams if they have the exact same character counts.",
      "Sort both character arrays or count character frequencies in an array of size 256."
    ],
    "sample_cases": [
      {
        "name": "act / cat",
        "input": "\"act\", \"cat\"",
        "expected": "1"
      },
      {
        "name": "CodeQuotient / QuotientCode",
        "input": "\"CodeQuotient\", \"QuotientCode\"",
        "expected": "1"
      },
      {
        "name": "Hello / Hillo",
        "input": "\"Hello\", \"Hillo\"",
        "expected": "0"
      }
    ],
    "display_number": 32,
    "display_id": "32",
    "languages": [
      "Java"
    ],
    "path_id": "strings",
    "path_name": "Strings",
    "order_in_path": 7,
    "collection_ids": [
      "company-amazon",
      "company-tcs",
      "college-placement"
    ],
    "review_needed": false
  },
  "strong-virus": {
    "id": "strong-virus",
    "title": "Strong Virus Detection",
    "summary": "A DNA sequence (any printable ASCII, may contain spaces) describes a virus. The virus is **strong** if it has an",
    "readme": "# Strong Virus Detection\n\n*Source: Practice-Test 1*\n\nA DNA sequence (any printable ASCII, may contain spaces) describes a virus. The virus is **strong** if it has an\n`x` and a `y` with **exactly three characters between them**. Return `true` if strong, else `false`.\n\n`boolean isStrongVirus(String dna)` in `class Virus` (instance method)\n\nExample: `txma yert` -> x at index 1, y at index 5, between them `m`, `a`, ` ` -> **YES**\n`BMuxp ioqytB yxurN` -> **NO**, `xaxoerylm` -> **YES**\n\nTotal length of all sequences <= 10^6.\n\nEdit `Solution.java`, then run:  `python3 judge.py strong-virus`\n",
    "solution": "class Virus {\n    // Returns true if the virus is strong, otherwise false\n    boolean isStrongVirus(String dna) {\n        // Write your code here\n        return false;\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "Strings",
      "Recursion"
    ],
    "hints": [
      "Find the first and last occurrence of target characters in the string.",
      "Check whether characters in between satisfy the contagion rule."
    ],
    "sample_cases": [
      {
        "name": "sample 1: txma yert",
        "input": "\"txma yert\"",
        "expected": "true"
      },
      {
        "name": "sample 2: BMuxp ioqytB yxurN",
        "input": "\"BMuxp ioqytB yxurN\"",
        "expected": "false"
      },
      {
        "name": "sample 3: xaxoerylm",
        "input": "\"xaxoerylm\"",
        "expected": "true"
      }
    ],
    "display_number": 33,
    "display_id": "33",
    "languages": [
      "Java"
    ],
    "path_id": "recursion",
    "path_name": "Recursion",
    "order_in_path": 1,
    "collection_ids": [
      "company-amazon",
      "exam-gate"
    ],
    "review_needed": false
  },
  "student-marks-get-element": {
    "id": "student-marks-get-element",
    "title": "Student Marks Management System",
    "summary": "Return the element at `index` as a **String**. If the index is invalid, **handle the exception** and return `Invalid Index`.",
    "readme": "# Student Marks Management System\n\n*Source: Practice-Test 14*\n\nReturn the element at `index` as a **String**. If the index is invalid, **handle the exception** and return `Invalid Index`.\n\n`public static String getElement(int arr[], int index)` in `class Main`\n\n`10 20 30 40 50`, index `2` -> `30`; index `7` -> `Invalid Index`\n\nEdit `Solution.java`, then run:  `python3 judge.py student-marks-get-element`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static String getElement(int arr[], int index)\n    {\n        // Students will implement this function\n        return \"\";\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Arrays",
      "Functions"
    ],
    "hints": [
      "Check array bounds before indexing, or catch ArrayIndexOutOfBoundsException.",
      "Return a custom error message or fallback value when index is invalid."
    ],
    "sample_cases": [
      {
        "name": "sample: index 2",
        "input": "a, 2",
        "expected": "30"
      },
      {
        "name": "sample: index 7",
        "input": "a, 7",
        "expected": "Invalid Index"
      },
      {
        "name": "first element",
        "input": "a, 0",
        "expected": "10"
      }
    ],
    "display_number": 34,
    "display_id": "34",
    "languages": [
      "Java"
    ],
    "path_id": "java-basics",
    "path_name": "Java Basics",
    "order_in_path": 4,
    "collection_ids": [
      "college-cuiet-lab",
      "exam-university"
    ],
    "review_needed": false
  },
  "sum-lower-triangle": {
    "id": "sum-lower-triangle",
    "title": "Sum of Lower Triangle of a Square Matrix",
    "summary": "Read `N` and an `N x N` matrix. Print the sum of the **lower triangle including the main diagonal** (elements with `col <= row`).",
    "readme": "# Sum of Lower Triangle of a Square Matrix\n\n*Source: Practice-Test 10*\n\nRead `N` and an `N x N` matrix. Print the sum of the **lower triangle including the main diagonal** (elements with `col <= row`).\n\n```\n3\n1 2 3\n4 5 6\n7 8 9\n```\nOutput `34` (1 + 4 + 5 + 7 + 8 + 9)\n\nConstraints: `1 <= N <= 5`, `-100 <= matrix[i][j] <= 100`\n\nEdit `Solution.java`, then run:  `python3 judge.py sum-lower-triangle`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // Write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Arrays",
      "Loops"
    ],
    "hints": [
      "The lower triangle of an N x N matrix contains elements where row >= col (i >= j).",
      "Iterate with outer loop i from 0 to N-1 and inner loop j from 0 to i."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "sample",
        "expected": "\"3\\n1 2 3\\n4 5 6\\n7 8 9\\n\", \"34\\n\", Test::go"
      },
      {
        "name": "1x1",
        "input": "1x1",
        "expected": "\"1\\n-7\\n\", \"-7\\n\", Test::go"
      },
      {
        "name": "2x2",
        "input": "2x2",
        "expected": "\"2\\n1 2\\n3 4\\n\", \"8\\n\", Test::go"
      }
    ],
    "display_number": 35,
    "display_id": "35",
    "languages": [
      "Java"
    ],
    "path_id": "sorting-searching",
    "path_name": "Sorting & Searching",
    "order_in_path": 8,
    "collection_ids": [
      "exam-university",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "sum-of-kth-row": {
    "id": "sum-of-kth-row",
    "title": "Sum of Elements in the Kth Row of a Matrix",
    "summary": "Read `R C`, the `R x C` matrix, then `K` (0-based). Print the sum of row `K`.",
    "readme": "# Sum of Elements in the Kth Row of a Matrix\n\n*Source: Practice-Test 8*\n\nRead `R C`, the `R x C` matrix, then `K` (0-based). Print the sum of row `K`.\n\n```\n3 5\n1 3 5 7 9\n2 4 6 8 10\n2 6 9 3 4\n2\n```\nOutput `24`\n\nConstraints: `1 <= R,C <= 100`, `0 <= K < R`, `-1000 <= matrix[i][j] <= 1000`\n\nEdit `Solution.java`, then run:  `python3 judge.py sum-of-kth-row`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String args[]) {\n        // Write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Arrays",
      "Loops"
    ],
    "hints": [
      "Access row K of the matrix: matrix[K].",
      "Sum all column elements across that specific row."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "sample",
        "expected": "\"3 5\\n1 3 5 7 9\\n2 4 6 8 10\\n2 6 9 3 4\\n2\\n\", \"24\\n\", Test::go"
      },
      {
        "name": "first row",
        "input": "first row",
        "expected": "\"3 5\\n1 3 5 7 9\\n2 4 6 8 10\\n2 6 9 3 4\\n0\\n\", \"25\\n\", Test::go"
      },
      {
        "name": "middle row",
        "input": "middle row",
        "expected": "\"3 5\\n1 3 5 7 9\\n2 4 6 8 10\\n2 6 9 3 4\\n1\\n\", \"30\\n\", Test::go"
      }
    ],
    "display_number": 36,
    "display_id": "36",
    "languages": [
      "Java"
    ],
    "path_id": "sorting-searching",
    "path_name": "Sorting & Searching",
    "order_in_path": 9,
    "collection_ids": [
      "exam-university",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "translate-the-letter": {
    "id": "translate-the-letter",
    "title": "Translate The Letter",
    "summary": "Reverse the **order of the words** in a sentence (words are separated by exactly one space, no leading/trailing spaces).",
    "readme": "# Translate The Letter\n\n*Source: Practice-Test 2*\n\nReverse the **order of the words** in a sentence (words are separated by exactly one space, no leading/trailing spaces).\n\n`static String translate(String letter)` in `class Result`\n\n`Code Loves Quotient Code` -> `Code Quotient Loves Code`\n`Coders Hello` -> `Hello Coders`\n\nConstraints: sentence length <= 100000\n\nEdit `Solution.java`, then run:  `python3 judge.py translate-the-letter`\n",
    "solution": "import java.util.*;\n\nclass Result {\n    static String translate(String letter) {\n        // Write your code here\n        return \"\";\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Strings",
      "Functions"
    ],
    "hints": [
      "Map specific characters to their replacement translation according to rules.",
      "Use a StringBuilder for efficient in-place string transformation."
    ],
    "sample_cases": [
      {
        "name": "sample 1",
        "input": "\"Code Loves Quotient Code\"",
        "expected": "Code Quotient Loves Code"
      },
      {
        "name": "sample 2",
        "input": "\"Coders Hello\"",
        "expected": "Hello Coders"
      },
      {
        "name": "single word",
        "input": "\"Single\"",
        "expected": "Single"
      }
    ],
    "display_number": 37,
    "display_id": "37",
    "languages": [
      "Java"
    ],
    "path_id": "java-basics",
    "path_name": "Java Basics",
    "order_in_path": 5,
    "collection_ids": [
      "company-wipro",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "tricycle-speed-manager": {
    "id": "tricycle-speed-manager",
    "title": "Tricycle Speed Manager",
    "summary": "`class Tricycle` with `private int speed`.",
    "readme": "# Tricycle Speed Manager\n\n*Source: Practice-Test 9*\n\n`class Tricycle` with `private int speed`.\n\n| Member | Behaviour |\n|---|---|\n| `Tricycle()` | speed = 5 |\n| `Tricycle(Tricycle t)` | copy of `t`'s speed (independent object) |\n| `void setSpeed(int s)` / `int getSpeed()` | set / get |\n| `void incr()` / `void brake()` | speed +1 / -1 |\n\nDriver: t1 default, incr; t2 = copy of t1, incr, setSpeed(x); brake both.\n\nEdit `Solution.java`, then run:  `python3 judge.py tricycle-speed-manager`\n",
    "solution": "import java.util.Scanner;\n\nclass Tricycle {\n    private int speed;\n\n    public Tricycle() {\n\n    }\n\n    public Tricycle(Tricycle t) {\n\n    }\n\n    public void setSpeed(int s) {\n\n    }\n\n    public int getSpeed() {\n        return 0;\n    }\n\n    public void incr() {\n\n    }\n\n    public void brake() {\n\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "OOP",
      "Functions"
    ],
    "hints": [
      "Encapsulate speed state within the Tricycle class.",
      "Provide methods to accelerate, decelerate, and validate non-negative speed."
    ],
    "sample_cases": [
      {
        "name": "default speed is 5",
        "input": ").getSpeed(",
        "expected": "5"
      },
      {
        "name": "incr",
        "input": "{ Tricycle t = new Tricycle(",
        "expected": "6"
      },
      {
        "name": "brake",
        "input": "{ Tricycle t = new Tricycle(",
        "expected": "4"
      }
    ],
    "display_number": 38,
    "display_id": "38",
    "languages": [
      "Java"
    ],
    "path_id": "oop",
    "path_name": "OOP",
    "order_in_path": 8,
    "collection_ids": [
      "college-cuiet-lab",
      "exam-viva"
    ],
    "review_needed": false
  },
  "uppercase-to-lowercase": {
    "id": "uppercase-to-lowercase",
    "title": "Convert Uppercase String to Lowercase",
    "summary": "Read a string of uppercase letters (A-Z, length 1..1000) and print it in lowercase.",
    "readme": "# Convert Uppercase String to Lowercase\n\n*Source: Practice-Test 3*\n\nRead a string of uppercase letters (A-Z, length 1..1000) and print it in lowercase.\n\n`CODEQUOTIENT` -> `codequotient`\n\nEdit `Solution.java`, then run:  `python3 judge.py uppercase-to-lowercase`\n",
    "solution": "import java.util.Scanner;\n\nclass Main {\n    public static void main(String[] args) {\n        // Write your code here\n    }\n}\n",
    "difficulty": "Easy",
    "topics": [
      "Strings",
      "Functions"
    ],
    "hints": [
      "Convert ASCII values by adding 32 or using Character.toLowerCase(c).",
      "Ensure characters already in lowercase or symbols remain unchanged."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "sample",
        "expected": "\"CODEQUOTIENT\\n\", \"codequotient\\n\", Test::go"
      },
      {
        "name": "single letter",
        "input": "single letter",
        "expected": "\"Q\\n\", \"q\\n\", Test::go"
      },
      {
        "name": "whole alphabet",
        "input": "whole alphabet",
        "expected": "\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\\n\", \"abcdefghijklmnopqrstuvwxyz\\n\", Test::go"
      }
    ],
    "display_number": 39,
    "display_id": "39",
    "languages": [
      "Java"
    ],
    "path_id": "java-basics",
    "path_name": "Java Basics",
    "order_in_path": 6,
    "collection_ids": [
      "company-wipro",
      "college-cuiet-lab"
    ],
    "review_needed": false
  },
  "valid-email-address": {
    "id": "valid-email-address",
    "title": "Valid email address",
    "summary": "Validate an email. It is **valid** only if it has exactly one `@`, exactly one `.`, the `.` comes **after** the `@`, and there is at least one character between `@` and `.`.",
    "readme": "# Valid email address\n\n*Source: Practice-Test 11*\n\nValidate an email. It is **valid** only if it has exactly one `@`, exactly one `.`, the `.` comes **after** the `@`, and there is at least one character between `@` and `.`.\nThrow the user-defined `EmailException` for an invalid address, **catch it inside** `isValidEmail`, and print `1` (valid) or `0` (invalid).\n\n`static void isValidEmail(String email)` in `class Main`\n\n`abc@gmail.com` -> 1, `email@codequotient` -> 0, `user.name@domain` -> 0, `student@college.edu` -> 1\n\nEdit `Solution.java`, then run:  `python3 judge.py valid-email-address`\n",
    "solution": "import java.util.Scanner;\n\nclass EmailException extends Exception {\n    EmailException() {\n        super();\n    }\n}\n\nclass Main {\n    static void isValidEmail(String email) {\n        //write your code here\n    }\n}\n",
    "difficulty": "Medium",
    "topics": [
      "Strings",
      "Functions"
    ],
    "hints": [
      "Validate format: must contain exactly one '@' followed by a valid domain with a '.'",
      "Ensure username and domain portions are non-empty and throw an exception for malformed emails."
    ],
    "sample_cases": [
      {
        "name": "abc@gmail.com",
        "input": "\"abc@gmail.com\"",
        "expected": "1\n"
      },
      {
        "name": "no dot after @",
        "input": "\"email@codequotient\"",
        "expected": "0\n"
      },
      {
        "name": "dot before @",
        "input": "\"user.name@domain\"",
        "expected": "0\n"
      }
    ],
    "display_number": 40,
    "display_id": "40",
    "languages": [
      "Java"
    ],
    "path_id": "strings",
    "path_name": "Strings",
    "order_in_path": 8,
    "collection_ids": [
      "company-capgemini",
      "company-infosys",
      "college-placement"
    ],
    "review_needed": false
  },
  "web-browser-tab-history": {
    "id": "web-browser-tab-history",
    "title": "Web Browser Tab History Analyzer",
    "summary": "Given a `LinkedList<Integer>` of website ids, return a **new** `LinkedList` of ids that appear **more than once**, each only once, in order of their **first appearance**. Do not modify the input. If none is frequent return an empty list.",
    "readme": "# Web Browser Tab History Analyzer\n\n*Source: Practice-Test 12*\n\nGiven a `LinkedList<Integer>` of website ids, return a **new** `LinkedList` of ids that appear **more than once**, each only once, in order of their **first appearance**. Do not modify the input. If none is frequent return an empty list.\n\n`public static LinkedList<Integer> findFrequentSites(LinkedList<Integer> history)` in `class Main`\n\n`101 205 310 101 450 205 101 520 310 600` -> `101 205 310`\n\nConstraints: `1 <= N <= 1000`, `100 <= id <= 999`\n\nEdit `Solution.java`, then run:  `python3 judge.py web-browser-tab-history`\n",
    "solution": "import java.util.*;\n\nclass Main {\n    public static LinkedList<Integer>\n    findFrequentSites(LinkedList<Integer> history) {\n\n        // Write your code here\n        return null;\n    }\n}\n",
    "difficulty": "Hard",
    "topics": [
      "OOP",
      "Recursion"
    ],
    "hints": [
      "Use two stacks: backStack and forwardStack.",
      "Visiting a new page pushes current page to backStack and clears forwardStack.",
      "Back pops from backStack onto forwardStack; forward pops from forwardStack onto backStack."
    ],
    "sample_cases": [
      {
        "name": "sample",
        "input": "ll(101,205,310,101,450,205,101,520,310,600)",
        "expected": "List.of(101, 205, 310)"
      },
      {
        "name": "no frequent site -> empty",
        "input": "ll(100,200,300)",
        "expected": "List.of()"
      },
      {
        "name": "all the same -> reported once",
        "input": "ll(100,100,100)",
        "expected": "List.of(100)"
      }
    ],
    "display_number": 41,
    "display_id": "41",
    "languages": [
      "Java"
    ],
    "path_id": "recursion",
    "path_name": "Recursion",
    "order_in_path": 2,
    "collection_ids": [
      "company-amazon",
      "exam-gate"
    ],
    "review_needed": false
  }
}
