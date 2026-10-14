import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("College Seats Are Reserved");
        Judge.eq("statement example 1", true, () -> Result.allSeatsFilled(new int[]{11,12,13,12,13}, new int[]{12,13,11,12,13}));
        Judge.eq("statement example 2", false, () -> Result.allSeatsFilled(new int[]{11,12,13}, new int[]{12,13,12}));
        Judge.eq("sample", true, () -> Result.allSeatsFilled(new int[]{11,12,13}, new int[]{12,11,13}));
        Judge.eq("single seat, same age", true, () -> Result.allSeatsFilled(new int[]{18}, new int[]{18}));
        Judge.eq("single seat, different age", false, () -> Result.allSeatsFilled(new int[]{18}, new int[]{19}));
        Judge.eq("same set, different counts", false, () -> Result.allSeatsFilled(new int[]{1,1,2}, new int[]{1,2,2}));
        Judge.eq("N = 10^5 shuffled", true, () -> { int[] a = new int[100000], b = new int[100000]; for (int i = 0; i < a.length; i++) { a[i] = i % 100 + 1; b[a.length - 1 - i] = a[i]; } return Result.allSeatsFilled(a, b); });
        Judge.eq("N = 10^5, one applicant differs", false, () -> { int[] a = new int[100000], b = new int[100000]; Arrays.fill(a, 50); Arrays.fill(b, 50); b[99999] = 51; return Result.allSeatsFilled(a, b); });
        Judge.end();
    }
}
