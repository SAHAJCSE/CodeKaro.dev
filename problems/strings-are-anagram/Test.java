import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Strings are anagram or not");
        Judge.eq("act / cat", 1, () -> Main.isAnagram("act", "cat"));
        Judge.eq("CodeQuotient / QuotientCode", 1, () -> Main.isAnagram("CodeQuotient", "QuotientCode"));
        Judge.eq("Hello / Hillo", 0, () -> Main.isAnagram("Hello", "Hillo"));
        Judge.eq("case sensitive", 0, () -> Main.isAnagram("Abc", "abc"));
        Judge.eq("different lengths", 0, () -> Main.isAnagram("aab", "ab"));
        Judge.eq("aabb / abab", 1, () -> Main.isAnagram("aabb", "abab"));
        Judge.eq("identical strings", 1, () -> Main.isAnagram("same", "same"));
        Judge.eq("same letters, different counts", 0, () -> Main.isAnagram("aabc", "abbc"));
        Judge.eq("100000 chars reversed", 1, () -> { String s = "abcdefghij".repeat(10000); return Main.isAnagram(s, new StringBuilder(s).reverse().toString()); });
        Judge.end();
    }
}
