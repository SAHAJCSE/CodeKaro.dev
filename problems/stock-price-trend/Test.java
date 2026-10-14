import java.util.*;

public class Test {
    static LinkedList<Integer> ll(Integer... v) { return new LinkedList<>(Arrays.asList(v)); }
    public static void main(String[] args) throws Exception {
        Judge.begin("Stock Trading - Price Trend Analyzer");
        Judge.eq("sample", List.of(520, 550, 580), () -> Main.findIncreasingPrices(ll(500,520,510,550,550,580,560)));
        Judge.eq("strictly decreasing -> empty", List.of(), () -> Main.findIncreasingPrices(ll(50,40,30,20)));
        Judge.eq("single price -> empty", List.of(), () -> Main.findIncreasingPrices(ll(100)));
        Judge.eq("strictly increasing", List.of(2, 3, 4), () -> Main.findIncreasingPrices(ll(1,2,3,4)));
        Judge.eq("equal prices are not an increase", List.of(), () -> Main.findIncreasingPrices(ll(5,5,5,5)));
        Judge.eq("original list is not modified", "[3, 1, 2]", () -> { LinkedList<Integer> p = ll(3,1,2); Main.findIncreasingPrices(p); return p.toString(); });
        Judge.eq("N = 1000 zig-zag", 499, () -> { Integer[] a = new Integer[1000]; for (int i = 0; i < 1000; i++) a[i] = i % 2 == 0 ? 10 : 20; a[0] = 30; return Main.findIncreasingPrices(ll(a)).size(); });
        Judge.end();
    }
}
