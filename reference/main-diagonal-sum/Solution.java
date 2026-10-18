import java.util.Scanner;

class Main {
    public static int mainDiagonalSum(int[][] matrix, int m) {
        int s = 0;
        for (int i = 0; i < m; i++) s += matrix[i][i];
        return s;
    }
}
