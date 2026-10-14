import java.util.Scanner;

class Main {
    public static String findLongestWord(String input) {
        String best = "";
        for (String w : input.split(" ")) if (w.length() > best.length()) best = w;
        return best;
    }
}
