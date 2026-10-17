import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Exam Topper");
        Judge.eq("sample 1", 93, () -> Result.maxMarks(new int[]{20,30,93,71,18,82,66}, 7));
        Judge.eq("sample 2 (max repeated)", 67, () -> Result.maxMarks(new int[]{33,45,67,33,67}, 5));
        Judge.eq("single element", -5, () -> Result.maxMarks(new int[]{-5}, 1));
        Judge.eq("all negative", -5, () -> Result.maxMarks(new int[]{-1000,-5,-999,-6}, 4));
        Judge.eq("all equal", 7, () -> Result.maxMarks(new int[]{7,7,7}, 3));
        Judge.eq("N = 100000, max at the end", 1000, () -> {
            int[] m = new int[100000]; for (int i = 0; i < m.length; i++) m[i] = (i % 1500) - 1000; m[99999] = 1000;
            return Result.maxMarks(m, 100000); });
        Judge.end();
    }
}
