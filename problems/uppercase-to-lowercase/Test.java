import java.util.*;

public class Test {
    static void go() throws Exception { Main.main(new String[0]); }

    public static void main(String[] args) throws Exception {
        Judge.begin("Convert Uppercase String to Lowercase");
        Judge.io("sample", "CODEQUOTIENT\n", "codequotient\n", Test::go);
        Judge.io("single letter", "Q\n", "q\n", Test::go);
        Judge.io("whole alphabet", "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n", "abcdefghijklmnopqrstuvwxyz\n", Test::go);
        Judge.io("length 1000", "Z".repeat(1000) + "\n", "z".repeat(1000) + "\n", Test::go);
        Judge.end();
    }
}
