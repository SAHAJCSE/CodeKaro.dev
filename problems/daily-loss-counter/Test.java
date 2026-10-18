import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("The Daily Loss Counter");
        Judge.eq("sample", 1, () -> Solution.count(new int[]{1,2,3,-5}, 4));
        Judge.eq("zero is not a loss", 0, () -> Solution.count(new int[]{0,0,0}, 3));
        Judge.eq("all losses", 3, () -> Solution.count(new int[]{-1,-2,-3}, 3));
        Judge.eq("mixed with zero", 1, () -> Solution.count(new int[]{0,-1,1}, 3));
        Judge.eq("extreme values", 1, () -> Solution.count(new int[]{1000000,-1000000}, 2));
        Judge.eq("T = 1000 alternating", 500, () -> { int[] a = new int[1000]; for (int i = 0; i < 1000; i++) a[i] = i % 2 == 0 ? 5 : -5; return Solution.count(a, 1000); });
        Judge.end();
    }
}
