import java.util.*;

class Main {
    static int isAnagram(String str1, String str2) {
        if (str1.length() != str2.length()) return 0;
        int[] f = new int[256];
        for (char c : str1.toCharArray()) f[c]++;
        for (char c : str2.toCharArray()) if (--f[c] < 0) return 0;
        return 1;
    }
}
