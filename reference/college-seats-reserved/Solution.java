import java.io.*;
import java.math.*;
import java.util.*;

class Result {
    static boolean allSeatsFilled(int[] A, int[] B) {
        if (A.length != B.length) return false;
        int[] f = new int[101];
        for (int x : A) f[x]++;
        for (int x : B) if (--f[x] < 0) return false;
        return true;
    }
}
