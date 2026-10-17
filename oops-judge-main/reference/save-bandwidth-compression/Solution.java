import java.util.*;

class Result {
    static String compressMsg(String textMsg) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < textMsg.length();) {
            int j = i; while (j < textMsg.length() && textMsg.charAt(j) == textMsg.charAt(i)) j++;
            sb.append(textMsg.charAt(i)); if (j - i > 1) sb.append(j - i);
            i = j;
        }
        return sb.toString();
    }
}
