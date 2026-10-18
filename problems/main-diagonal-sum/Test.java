import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Find sum of main diagonal of matrix");
        Judge.eq("sample", 15, () -> Main.mainDiagonalSum(new int[][]{{1,2,3},{4,5,6},{7,8,9}}, 3));
        Judge.eq("1x1", -4, () -> Main.mainDiagonalSum(new int[][]{{-4}}, 1));
        Judge.eq("negatives", -15, () -> Main.mainDiagonalSum(new int[][]{{-1,2,3},{4,-5,6},{7,8,-9}}, 3));
        Judge.eq("2x2", 5, () -> Main.mainDiagonalSum(new int[][]{{1,100},{100,4}}, 2));
        Judge.eq("4x4 (anti-diagonal differs)", 34, () -> Main.mainDiagonalSum(new int[][]{{1,9,9,4},{9,6,7,9},{9,8,11,9},{2,9,9,16}}, 4));
        Judge.end();
    }
}
