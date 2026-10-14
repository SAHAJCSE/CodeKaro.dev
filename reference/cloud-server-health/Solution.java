import java.util.*;

class Main {
    public static ArrayList<Integer> findOverloadedServers(ArrayList<Integer> cpuUsage) {
        ArrayList<Integer> r = new ArrayList<>();
        for (int x : cpuUsage) if (x >= 80) r.add(x);
        return r;
    }
}
