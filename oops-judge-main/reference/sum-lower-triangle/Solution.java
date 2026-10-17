import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), s = 0;
        for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) { int v = sc.nextInt(); if (j <= i) s += v; }
        System.out.println(s);
    }
}
