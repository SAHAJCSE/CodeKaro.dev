import java.util.*;

public class Test {
    static String big(boolean rev) { List<String> w = new ArrayList<>();
        for (int i = 0; i < 33333; i++) w.add("w" .substring(0,1) + (char)('a' + i % 26) + (char)('a' + (i / 26) % 26));
        if (rev) Collections.reverse(w); return String.join(" ", w); }
    public static void main(String[] args) throws Exception {
        Judge.begin("Translate The Letter");
        Judge.eq("sample 1", "Code Quotient Loves Code", () -> Result.translate("Code Loves Quotient Code"));
        Judge.eq("sample 2", "Hello Coders", () -> Result.translate("Coders Hello"));
        Judge.eq("single word", "Single", () -> Result.translate("Single"));
        Judge.eq("letters", "e d c b a", () -> Result.translate("a b c d e"));
        Judge.eq("mixed case kept", "World hello Big", () -> Result.translate("Big hello World"));
        Judge.eq("33333 words", big(true), () -> Result.translate(big(false)));
        Judge.end();
    }
}
