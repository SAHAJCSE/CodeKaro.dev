import java.util.*;

class Main {
    public static LinkedList<Integer> findFrequentSites(LinkedList<Integer> history) {
        Map<Integer, Integer> cnt = new LinkedHashMap<>();
        for (int x : history) cnt.merge(x, 1, Integer::sum);
        LinkedList<Integer> r = new LinkedList<>();
        for (Map.Entry<Integer, Integer> e : cnt.entrySet()) if (e.getValue() > 1) r.add(e.getKey());
        return r;
    }
}
