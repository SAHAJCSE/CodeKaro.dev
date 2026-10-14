import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Compress a string");
        Judge.eq("sample 1", "a2b2c2def", () -> Main.compressString("aabbccdef"));
        Judge.eq("sample 2", "abd7", () -> Main.compressString("abddddddd"));
        Judge.eq("no repeats", "abc", () -> Main.compressString("abc"));
        Judge.eq("single char", "x", () -> Main.compressString("x"));
        Judge.eq("whole string one char", "a4", () -> Main.compressString("aaaa"));
        Judge.eq("three groups", "a3b3c3", () -> Main.compressString("aaabbbccc"));
        Judge.eq("alternating (no compression)", "abab", () -> Main.compressString("abab"));
        Judge.eq("run of 10 -> two digits", "a10", () -> Main.compressString("aaaaaaaaaa"));
        Judge.end();
    }
}
