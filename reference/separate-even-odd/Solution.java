import java.util.*;

class Main {
    static void separate(int a[], int n) {
        StringBuilder e = new StringBuilder(), o = new StringBuilder();
        for (int i = 0; i < n; i++) {
            StringBuilder t = a[i] % 2 == 0 ? e : o;
            if (t.length() > 0) t.append(' ');
            t.append(a[i]);
        }
        System.out.println(e); System.out.println(o);
    }
}
