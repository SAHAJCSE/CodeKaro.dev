import java.io.*;
import java.util.*;

class Result {
    public static boolean isPerfect(String str) {
        int ab = 0, xy = 0;
        for (char c : str.toCharArray()) { if (c == 'a' || c == 'b') ab++; else if (c == 'x' || c == 'y') xy++; }
        return ab % 2 == 1 && xy % 2 == 0;
    }
}
