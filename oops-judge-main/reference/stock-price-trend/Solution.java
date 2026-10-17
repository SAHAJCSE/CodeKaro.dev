import java.util.*;

class Main {
    public static LinkedList<Integer> findIncreasingPrices(LinkedList<Integer> prices) {
        LinkedList<Integer> r = new LinkedList<>();
        Integer prev = null;
        for (int p : prices) { if (prev != null && p > prev) r.add(p); prev = p; }
        return r;
    }
}
