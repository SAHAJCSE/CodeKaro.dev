import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int k = n; k >= 1; k--) { for (int j = 1; j <= k; j++) System.out.print(j); System.out.println(); }
    }
}
