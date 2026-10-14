import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Quality Check (even / odd count)");
        Judge.out("sample", "1 3\n", () -> Solution.count(new int[]{1,3,5,8}, 4));
        Judge.out("all even", "3 0\n", () -> Solution.count(new int[]{2,4,6}, 3));
        Judge.out("all odd", "0 5\n", () -> Solution.count(new int[]{1,1,1,1,1}, 5));
        Judge.out("balanced", "3 3\n", () -> Solution.count(new int[]{10,20,30,41,51,61}, 6));
        Judge.out("large values", "1 1\n", () -> Solution.count(new int[]{100000,99999}, 2));
        Judge.end();
    }
}
