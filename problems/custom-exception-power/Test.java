import java.util.*;

public class Test {
    static String p(int n, int e) { try { return String.valueOf(Main.power(n, e)); } catch (CustomException ex) { return "EX: " + ex.getMessage(); } }
    public static void main(String[] args) throws Exception {
        Judge.begin("Calculate positive power of a positive number");
        Judge.eq("2^2 = 4", "4", () -> p(2, 2));
        Judge.eq("both negative", "EX: Negative numbers not allowed", () -> p(-4, -5));
        Judge.eq("negative base", "EX: Negative numbers not allowed", () -> p(-2, 3));
        Judge.eq("negative exponent", "EX: Negative numbers not allowed", () -> p(2, -3));
        Judge.eq("both zero", "EX: Both can never be zero", () -> p(0, 0));
        Judge.eq("5^0 = 1", "1", () -> p(5, 0));
        Judge.eq("0^5 = 0", "0", () -> p(0, 5));
        Judge.eq("3^4 = 81", "81", () -> p(3, 4));
        Judge.eq("negative check wins over zero check", "EX: Negative numbers not allowed", () -> p(0, -1));
        Judge.end();
    }
}
