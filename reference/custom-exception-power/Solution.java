import java.util.Scanner;

class CustomException extends Exception {
    private String msg;
    public CustomException(String message) { this.msg = message; }
    @Override public String getMessage() { return msg; }
}

class Main {
    static int power(int num, int exp) throws CustomException {
        if (num < 0 || exp < 0) throw new CustomException("Negative numbers not allowed");
        if (num == 0 && exp == 0) throw new CustomException("Both can never be zero");
        int r = 1; for (int i = 0; i < exp; i++) r *= num;
        return r;
    }
}
