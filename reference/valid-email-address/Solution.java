import java.util.Scanner;

class EmailException extends Exception {
    EmailException() {
        super();
    }
}

class Main {
    static void isValidEmail(String email) {
        try {
            int at = email.indexOf('@'), dot = email.indexOf('.');
            if (at < 0 || at != email.lastIndexOf('@')) throw new EmailException();
            if (dot < 0 || dot != email.lastIndexOf('.')) throw new EmailException();
            if (dot <= at + 1) throw new EmailException();
            System.out.println(1);
        } catch (EmailException e) {
            System.out.println(0);
        }
    }
}
