import java.util.*;

public class Test {
    static void go() throws Exception { Main.main(new String[0]); }
    static String exp(int n) { StringBuilder sb = new StringBuilder(); int c = 1;
        for (int i = 1; i <= n; i++) { for (int j = 0; j < i; j++) { if (j > 0) sb.append(' '); sb.append(c++); } sb.append('\n'); }
        return sb.toString(); }
    public static void main(String[] args) throws Exception {
        Judge.begin("Sequential ID Pyramid - 7");
        Judge.io("n = 3", "3\n", "1\n2 3\n4 5 6\n", Test::go);
        Judge.io("n = 1", "1\n", "1\n", Test::go);
        Judge.io("n = 4", "4\n", "1\n2 3\n4 5 6\n7 8 9 10\n", Test::go);
        Judge.io("n = 50", "50\n", exp(50), Test::go);
        Judge.end();
    }
}
