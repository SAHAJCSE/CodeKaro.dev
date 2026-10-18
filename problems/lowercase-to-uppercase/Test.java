import java.util.*;

public class Test {
    static void go() throws Exception { Main.main(new String[0]); }

    public static void main(String[] args) throws Exception {
        Judge.begin("Convert lower case to upper case");
        Judge.io("sample", "codequotient\n", "CODEQUOTIENT\n", Test::go);
        Judge.io("single letter", "q\n", "Q\n", Test::go);
        Judge.io("whole alphabet", "abcdefghijklmnopqrstuvwxyz\n", "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n", Test::go);
        Judge.io("length 1000", "z".repeat(1000) + "\n", "Z".repeat(1000) + "\n", Test::go);
        Judge.end();
    }
}
