import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Strong Virus Detection");
        Virus v = new Virus();
        Judge.eq("sample 1: txma yert", true, () -> v.isStrongVirus("txma yert"));
        Judge.eq("sample 2: BMuxp ioqytB yxurN", false, () -> v.isStrongVirus("BMuxp ioqytB yxurN"));
        Judge.eq("sample 3: xaxoerylm", true, () -> v.isStrongVirus("xaxoerylm"));
        Judge.eq("x and y adjacent", false, () -> v.isStrongVirus("xy"));
        Judge.eq("three spaces between", true, () -> v.isStrongVirus("x   y"));
        Judge.eq("four chars between", false, () -> v.isStrongVirus("xabcdy"));
        Judge.eq("two chars between", false, () -> v.isStrongVirus("xabyz"));
        Judge.eq("no x / no y", false, () -> v.isStrongVirus("aaaaaaaaaa"));
        Judge.eq("x repeated, second one matches", true, () -> v.isStrongVirus("xyxabcy"));
        Judge.eq("length 10^6, no match", false, () -> v.isStrongVirus("a".repeat(1000000)));
        Judge.eq("length 10^6, match at the end", true, () -> v.isStrongVirus("a".repeat(999995) + "xabcy"));
        Judge.end();
    }
}
