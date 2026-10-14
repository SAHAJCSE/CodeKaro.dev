import java.util.Scanner;

class MyException extends Exception {
    int code;

    MyException(int code) {
        this.code = code;
    }
}

class Main {
    static void power(int n, int p) {
        try {
            if (n < 0 || p < 0) throw new MyException(-1);
            if (n == 0 && p == 0) throw new MyException(-2);
            long r = 1; for (int i = 0; i < p; i++) r *= n;
            System.out.println(r);
        } catch (MyException e) {
            System.out.println(e.code);
        }
    }
}
