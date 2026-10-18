import java.util.*;

public class Test {
    static void go() throws Exception { Main.main(new String[0]); }

    public static void main(String[] args) throws Exception {
        Judge.begin("Sum of Elements in the Kth Row of a Matrix");
        Judge.io("sample", "3 5\n1 3 5 7 9\n2 4 6 8 10\n2 6 9 3 4\n2\n", "24\n", Test::go);
        Judge.io("first row", "3 5\n1 3 5 7 9\n2 4 6 8 10\n2 6 9 3 4\n0\n", "25\n", Test::go);
        Judge.io("middle row", "3 5\n1 3 5 7 9\n2 4 6 8 10\n2 6 9 3 4\n1\n", "30\n", Test::go);
        Judge.io("1x1", "1 1\n-8\n0\n", "-8\n", Test::go);
        Judge.io("negatives", "2 3\n-1 -2 -3\n4 5 -6\n0\n", "-6\n", Test::go);
        Judge.io("single column", "3 1\n4\n5\n6\n1\n", "5\n", Test::go);
        Judge.end();
    }
}
