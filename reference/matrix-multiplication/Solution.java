class Main {
    public static int[][] multiply(int[][] A, int[][] B, int R1, int C1, int C2) {
        int[][] r = new int[R1][C2];
        for (int i = 0; i < R1; i++) for (int j = 0; j < C2; j++) for (int k = 0; k < C1; k++) r[i][j] += A[i][k] * B[k][j];
        return r;
    }
}
