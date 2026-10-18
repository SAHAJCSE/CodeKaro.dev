import java.util.*;

class Result {
    static String translate(String letter) {
        String[] w = letter.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = w.length - 1; i >= 0; i--) { sb.append(w[i]); if (i > 0) sb.append(' '); }
        return sb.toString();
    }
}
