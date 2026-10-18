import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("MyCalculator Exception");
        Judge.out("2^3 = 8", "8\n", () -> Main.power(2, 3));
        Judge.out("negative n", "-1\n", () -> Main.power(-3, 2));
        Judge.out("both zero", "-2\n", () -> Main.power(0, 0));
        Judge.out("5^0 = 1", "1\n", () -> Main.power(5, 0));
        Judge.out("0^5 = 0", "0\n", () -> Main.power(0, 5));
        Judge.out("negative p", "-1\n", () -> Main.power(4, -1));
        Judge.out("both negative", "-1\n", () -> Main.power(-1, -1));
        Judge.out("2^10 = 1024", "1024\n", () -> Main.power(2, 10));
        Judge.out("1^0 = 1", "1\n", () -> Main.power(1, 0));
        Judge.end();
    }
}
