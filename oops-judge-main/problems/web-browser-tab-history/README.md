# Web Browser Tab History Analyzer

*Source: Practice-Test 12*

Given a `LinkedList<Integer>` of website ids, return a **new** `LinkedList` of ids that appear **more than once**, each only once, in order of their **first appearance**. Do not modify the input. If none is frequent return an empty list.

`public static LinkedList<Integer> findFrequentSites(LinkedList<Integer> history)` in `class Main`

`101 205 310 101 450 205 101 520 310 600` -> `101 205 310`

Constraints: `1 <= N <= 1000`, `100 <= id <= 999`

Edit `Solution.java`, then run:  `python3 judge.py web-browser-tab-history`
