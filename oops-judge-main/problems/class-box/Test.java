import java.util.*;

public class Test {
    static String d(Box b) { return b.getLength() + " " + b.getBreadth() + " " + b.getHeight() + " " + b.CalculateVolume(); }
    public static void main(String[] args) throws Exception {
        Judge.begin("class - Box");
        Judge.eq("default constructor", "0 0 0 0", () -> d(new Box()));
        Judge.eq("parameterised constructor (sample)", "3 4 5 60", () -> d(new Box(3, 4, 5)));
        Judge.eq("copy constructor (sample)", "3 4 5 60", () -> d(new Box(new Box(3, 4, 5))));
        Judge.eq("copy of default", "0 0 0 0", () -> d(new Box(new Box())));
        Judge.eq("zero dimension", "7 0 9 0", () -> d(new Box(7, 0, 9)));
        Judge.eq("volume needs long (10^5)^3", 1000000000000000L, () -> new Box(100000, 100000, 100000).CalculateVolume());
        Judge.eq("getters are in the right order", "1 2 3", () -> { Box b = new Box(1, 2, 3); return b.getLength() + " " + b.getBreadth() + " " + b.getHeight(); });
        Judge.end();
    }
}
