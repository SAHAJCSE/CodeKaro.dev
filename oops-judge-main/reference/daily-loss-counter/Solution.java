import java.util.*;
import java.io.*;

class Solution {
    public static int count(int[] a, int T) {
        int c = 0;
        for (int i = 0; i < T; i++) if (a[i] < 0) c++;
        return c;
    }
}
