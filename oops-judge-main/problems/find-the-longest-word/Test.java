import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Find the Longest Word");
        Judge.eq("sample", "programming", () -> Main.findLongestWord("I love programming"));
        Judge.eq("single word", "hello", () -> Main.findLongestWord("hello"));
        Judge.eq("longest in the middle", "ccc", () -> Main.findLongestWord("a bb ccc dd e"));
        Judge.eq("longest first", "Elephant", () -> Main.findLongestWord("Elephant is big"));
        Judge.eq("longest last", "Extraordinary", () -> Main.findLongestWord("I am Extraordinary"));
        Judge.eq("sentence of 10^5 chars", "z".repeat(50), () -> Main.findLongestWord("ab ".repeat(33000) + "z".repeat(50)));
        Judge.end();
    }
}
