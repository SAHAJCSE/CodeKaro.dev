import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Save Bandwidth Using Compression");
        Judge.eq("sample 1", "a2b2c2def", () -> Result.compressMsg("aabbccdef"));
        Judge.eq("sample 2", "abd7", () -> Result.compressMsg("abddddddd"));
        Judge.eq("no repeats", "abc", () -> Result.compressMsg("abc"));
        Judge.eq("single char", "x", () -> Result.compressMsg("x"));
        Judge.eq("whole string one char", "a4", () -> Result.compressMsg("aaaa"));
        Judge.eq("three groups", "a3b3c3", () -> Result.compressMsg("aaabbbccc"));
        Judge.eq("alternating (no compression)", "abab", () -> Result.compressMsg("abab"));
        Judge.eq("run of 10 -> two digits", "a10", () -> Result.compressMsg("aaaaaaaaaa"));
        Judge.eq("sample (runs repeat later)", "g2k2gd3g4", () -> Result.compressMsg("ggkkgdddgggg"));
        Judge.eq("same char reappears", "a2ba2", () -> Result.compressMsg("aabaa"));
        Judge.eq("12 z's", "z12", () -> Result.compressMsg("zzzzzzzzzzzz"));
        Judge.end();
    }
}
