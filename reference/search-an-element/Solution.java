import java.util.Scanner;

class Search {
    static int SearchElement(int[] arr, int ele) {
        int c = 0;
        for (int x : arr) if (x == ele) c++;
        return c == 0 ? -1 : c;
    }
}
