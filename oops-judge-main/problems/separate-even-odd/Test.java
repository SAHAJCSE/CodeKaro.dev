import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Put even and odd elements in 2 separate arrays");
        Judge.out("sample", "8\n1 3 5\n", () -> Main.separate(new int[]{1,3,5,8}, 4));
        Judge.out("order is preserved", "2 4\n1 3\n", () -> Main.separate(new int[]{2,1,4,3}, 4));
        Judge.out("negative numbers and zero", "10 -8 0\n-3 7 5\n", () -> Main.separate(new int[]{10,-3,7,-8,0,5}, 6));
        Judge.out("single even + single odd", "2\n1\n", () -> Main.separate(new int[]{1,2}, 2));
        Judge.out("large values", "1000000000 -1000000000\n999999999 -999999999\n", () -> Main.separate(new int[]{1000000000,999999999,-1000000000,-999999999}, 4));
        Judge.end();
    }
}
