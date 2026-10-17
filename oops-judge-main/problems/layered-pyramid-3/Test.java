import java.util.*;

public class Test {
    static void go() throws Exception { Main.main(new String[0]); }
    static String stars(int k) { StringBuilder s = new StringBuilder(); for (int i = 0; i < k; i++) s.append('*'); return s.toString(); }
    static String digits(int from, int to) { StringBuilder s = new StringBuilder();
        if (from <= to) for (int i = from; i <= to; i++) s.append(i); else for (int i = from; i >= to; i--) s.append(i); return s.toString(); }
    static String exp(int n) { StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) sb.append(stars(n - i)).append(digits(1, i)).append('\n');
        return sb.toString(); }
    public static void main(String[] args) throws Exception {
        Judge.begin("Layered Calibration Code Pyramid - 3");
        Judge.io("n = 5", "5\n", exp(5), Test::go);
        Judge.io("n = 3", "3\n", exp(3), Test::go);
        Judge.io("n = 1", "1\n", exp(1), Test::go);
        Judge.io("n = 9", "9\n", exp(9), Test::go);
        Judge.end();
    }
}
