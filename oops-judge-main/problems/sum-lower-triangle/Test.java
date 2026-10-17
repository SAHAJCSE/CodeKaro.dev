import java.util.*;

public class Test {
    static void go() throws Exception { Main.main(new String[0]); }

    public static void main(String[] args) throws Exception {
        Judge.begin("Sum of Lower Triangle of a Square Matrix");
        Judge.io("sample", "3\n1 2 3\n4 5 6\n7 8 9\n", "34\n", Test::go);
        Judge.io("1x1", "1\n-7\n", "-7\n", Test::go);
        Judge.io("2x2", "2\n1 2\n3 4\n", "8\n", Test::go);
        Judge.io("negative values", "2\n-5 100\n-3 -4\n", "-12\n", Test::go);
        Judge.io("5x5", "5\n1 1 1 1 1\n2 2 2 2 2\n3 3 3 3 3\n4 4 4 4 4\n5 5 5 5 5\n", "55\n", Test::go);
        Judge.end();
    }
}
