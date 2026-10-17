import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Perfect String");
        Judge.eq("sample 1: xaxbyyb", true, () -> Result.isPerfect("xaxbyyb"));
        Judge.eq("sample 2: aabbxxyy", false, () -> Result.isPerfect("aabbxxyy"));
        Judge.eq("sample 3: abaabxy", true, () -> Result.isPerfect("abaabxy"));
        Judge.eq("sample 4: yyxaby", false, () -> Result.isPerfect("yyxaby"));
        Judge.eq("odd a+b, even x+y", true, () -> Result.isPerfect("axx"));
        Judge.eq("odd a+b, odd x+y", false, () -> Result.isPerfect("ax"));
        Judge.eq("even a+b, even x+y", false, () -> Result.isPerfect("abxy"));
        Judge.eq("long string", true, () -> Result.isPerfect("a" + "xy".repeat(50000)));
        Judge.end();
    }
}
