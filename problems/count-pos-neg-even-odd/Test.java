import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Count negative, positive, even and odd");
        Judge.out("sample", "7\n3\n5\n5\n", () -> Result.countAndPrint(new int[]{-3,10,20,-4,7,1,-2,3,4,5}, 10));
        Judge.out("with zeros", "4\n4\n6\n4\n", () -> Result.countAndPrint(new int[]{0,0,1,-1,2,-2,3,-3,4,-4}, 10));
        Judge.out("all positive", "10\n0\n5\n5\n", () -> Result.countAndPrint(new int[]{1,2,3,4,5,6,7,8,9,10}, 10));
        Judge.out("all negative odd", "0\n10\n0\n10\n", () -> Result.countAndPrint(new int[]{-1,-3,-5,-7,-9,-11,-13,-15,-17,-19}, 10));
        Judge.out("all zero", "0\n0\n10\n0\n", () -> Result.countAndPrint(new int[10], 10));
        Judge.end();
    }
}
