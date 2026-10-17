import java.util.*;

public class Test {
    static ArrayList<Integer> al(Integer... v) { return new ArrayList<>(Arrays.asList(v)); }
    public static void main(String[] args) throws Exception {
        Judge.begin("Library Book Inventory Management");
        Judge.eq("sample", List.of(101,102,103,104,105,106,107), () -> Main.updateInventory(al(101,102,103,104), new int[]{104,105,106,102,107}));
        Judge.eq("statement example", List.of(101,102,103,104,105,106), () -> Main.updateInventory(al(101,102,103), new int[]{102,104,105,101,106}));
        Judge.eq("all already present", List.of(1,2,3), () -> Main.updateInventory(al(1,2,3), new int[]{3,2,1}));
        Judge.eq("duplicates inside the new books", List.of(5,9), () -> Main.updateInventory(al(5), new int[]{9,9,9,5}));
        Judge.eq("all new, order kept", List.of(1,30,20,10), () -> Main.updateInventory(al(1), new int[]{30,20,10}));
        Judge.eq("no new books", List.of(7,8), () -> Main.updateInventory(al(7,8), new int[]{}));
        Judge.end();
    }
}
