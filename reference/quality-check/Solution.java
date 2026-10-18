import java.util.*;

class Solution {
    static void count(int[] a, int T) {
        int e = 0, o = 0;
        for (int i = 0; i < T; i++) if (a[i] % 2 == 0) e++; else o++;
        System.out.println(e + " " + o);
    }
}
