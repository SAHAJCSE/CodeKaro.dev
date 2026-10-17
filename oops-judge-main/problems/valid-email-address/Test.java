import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Valid email address");
        Judge.out("abc@gmail.com", "1\n", () -> Main.isValidEmail("abc@gmail.com"));
        Judge.out("no dot after @", "0\n", () -> Main.isValidEmail("email@codequotient"));
        Judge.out("dot before @", "0\n", () -> Main.isValidEmail("user.name@domain"));
        Judge.out("student@college.edu", "1\n", () -> Main.isValidEmail("student@college.edu"));
        Judge.out("shortest valid a@b.c", "1\n", () -> Main.isValidEmail("a@b.c"));
        Judge.out("nothing between @ and .", "0\n", () -> Main.isValidEmail("a@.c"));
        Judge.out("two @", "0\n", () -> Main.isValidEmail("abc@@gmail.com"));
        Judge.out("two dots", "0\n", () -> Main.isValidEmail("abc@gmail.co.in"));
        Judge.out("no @ at all", "0\n", () -> Main.isValidEmail("abc.gmail"));
        Judge.out("plain text", "0\n", () -> Main.isValidEmail("plain"));
        Judge.end();
    }
}
