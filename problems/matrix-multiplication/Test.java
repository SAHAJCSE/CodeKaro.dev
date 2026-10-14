import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Matrix Multiplication");
        Judge.eq("sample test 1", new int[][]{{10,10},{25,28}}, () -> Main.multiply(new int[][]{{1,2,3},{4,5,6}}, new int[][]{{2,3},{1,2},{2,1}}, 2, 3, 2));
        Judge.eq("sample test 2", new int[][]{{36,68,100},{32,58,84}}, () -> Main.multiply(new int[][]{{12,4},{7,6}}, new int[][]{{2,4,6},{3,5,7}}, 2, 2, 3));
        Judge.eq("1x1", new int[][]{{-6}}, () -> Main.multiply(new int[][]{{2}}, new int[][]{{-3}}, 1, 1, 1));
        Judge.eq("negative numbers", new int[][]{{9,10},{-13,-14}}, () -> Main.multiply(new int[][]{{-1,2},{3,-4}}, new int[][]{{5,6},{7,8}}, 2, 2, 2));
        Judge.eq("identity", new int[][]{{1,2},{3,4}}, () -> Main.multiply(new int[][]{{1,2},{3,4}}, new int[][]{{1,0},{0,1}}, 2, 2, 2));
        Judge.eq("matrix x column vector", new int[][]{{-2},{-2}}, () -> Main.multiply(new int[][]{{1,2,3},{4,5,6}}, new int[][]{{1},{0},{-1}}, 2, 3, 1));
        Judge.end();
    }
}
