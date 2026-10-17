import java.util.*;

public class Test {
    static void go() throws Exception { Main.main(new String[0]); }

    public static void main(String[] args) throws Exception {
        Judge.begin("Sum of elements of matrix");
        Judge.io("sample 2", "2\n3\n1 2 3\n4 5 6\n0\n0\n", "11\n", Test::go);
        Judge.io("3x3, row 1 + column 2", "3\n3\n1 2 3\n2 2 2\n4 5 3\n1\n2\n", "14\n", Test::go);
        Judge.io("1x1", "1\n1\n5\n0\n0\n", "10\n", Test::go);
        Judge.io("negative numbers", "2\n2\n-1 -2\n-3 -4\n1\n0\n", "-11\n", Test::go);
        Judge.io("last row / last column", "3\n2\n1 2\n3 4\n5 6\n2\n1\n", "23\n", Test::go);
        Judge.end();
    }
}
