import java.util.*;

public class Test {
    static LinkedList<Integer> ll(Integer... v) { return new LinkedList<>(Arrays.asList(v)); }
    public static void main(String[] args) throws Exception {
        Judge.begin("Web Browser Tab History Analyzer");
        Judge.eq("sample", List.of(101, 205, 310), () -> Main.findFrequentSites(ll(101,205,310,101,450,205,101,520,310,600)));
        Judge.eq("no frequent site -> empty", List.of(), () -> Main.findFrequentSites(ll(100,200,300)));
        Judge.eq("all the same -> reported once", List.of(100), () -> Main.findFrequentSites(ll(100,100,100)));
        Judge.eq("first-appearance order, not sorted", List.of(500, 300), () -> Main.findFrequentSites(ll(500,300,500,300,200)));
        Judge.eq("single entry", List.of(), () -> Main.findFrequentSites(ll(555)));
        Judge.eq("original list is not modified", "[7, 8, 7, 9, 8]", () -> { LinkedList<Integer> h = ll(7,8,7,9,8); Main.findFrequentSites(h); return h.toString(); });
        Judge.eq("N = 1000 (100 ids repeat)", 100, () -> { Integer[] a = new Integer[1000]; for (int i = 0; i < 1000; i++) a[i] = 100 + i % 900; return Main.findFrequentSites(ll(a)).size(); });
        Judge.end();
    }
}
