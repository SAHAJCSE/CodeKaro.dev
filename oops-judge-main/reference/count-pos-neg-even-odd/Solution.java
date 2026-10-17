import java.util.Scanner;

class Result {
    static void countAndPrint(int[] arr, int n) {
        int p = 0, ng = 0, e = 0, o = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] > 0) p++; else if (arr[i] < 0) ng++;
            if (arr[i] % 2 == 0) e++; else o++;
        }
        System.out.println(p); System.out.println(ng); System.out.println(e); System.out.println(o);
    }
}
