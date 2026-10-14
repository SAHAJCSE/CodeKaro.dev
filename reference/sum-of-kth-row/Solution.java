import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt(), c = sc.nextInt();
        int[][] m = new int[r][c];
        for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) m[i][j] = sc.nextInt();
        int k = sc.nextInt(), s = 0;
        for (int j = 0; j < c; j++) s += m[k][j];
        System.out.println(s);
    }
}
