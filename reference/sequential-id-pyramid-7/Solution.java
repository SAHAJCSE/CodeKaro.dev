import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt(), c = 1;
        for (int i = 1; i <= n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < i; j++) { if (j > 0) sb.append(' '); sb.append(c++); }
            System.out.println(sb);
        }
    }
}
