import java.util.*;

public class Test {
    static String cat(String a, String b, int extra) { char[] r = new char[a.length() + b.length() + extra];
        Main.strcat(r, a.toCharArray(), b.toCharArray()); return new String(r, 0, a.length() + b.length()); }
    public static void main(String[] args) throws Exception {
        Judge.begin("The Airline Ticket - Concatenate two strings");
        Judge.eq("Code + Quotient", "CodeQuotient", () -> cat("Code", "Quotient", 0));
        Judge.eq("John + Doe", "JohnDoe", () -> cat("John", "Doe", 0));
        Judge.eq("single chars", "ab", () -> cat("a", "b", 0));
        Judge.eq("result array larger than needed", "HelloWorld", () -> cat("Hello", "World", 6));
        Judge.eq("different lengths", "ABCDEFGHIJKLMNOPQRSTUVWXYZ!", () -> cat("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "!", 0));
        Judge.end();
    }
}
