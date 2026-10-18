import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Cloud Server Health Monitoring");
        Judge.eq("sample", List.of(82, 95, 88), () -> Main.findOverloadedServers(new ArrayList<>(List.of(45,82,67,95,79,88,60))));
        Judge.eq("exactly 80 counts", List.of(80, 81), () -> Main.findOverloadedServers(new ArrayList<>(List.of(80,79,81))));
        Judge.eq("none overloaded", List.of(), () -> Main.findOverloadedServers(new ArrayList<>(List.of(10,20,79))));
        Judge.eq("all overloaded", List.of(100, 80, 90), () -> Main.findOverloadedServers(new ArrayList<>(List.of(100,80,90))));
        Judge.eq("single server", List.of(99), () -> Main.findOverloadedServers(new ArrayList<>(List.of(99))));
        Judge.end();
    }
}
