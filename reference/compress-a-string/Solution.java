import java.util.Scanner;

class Main {
    public static String compressString(String str) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length();) {
            int j = i; while (j < str.length() && str.charAt(j) == str.charAt(i)) j++;
            sb.append(str.charAt(i)); if (j - i > 1) sb.append(j - i);
            i = j;
        }
        return sb.toString();
    }
}
