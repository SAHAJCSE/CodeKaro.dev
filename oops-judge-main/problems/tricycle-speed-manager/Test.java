import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Tricycle Speed Manager");
        Judge.eq("default speed is 5", 5, () -> new Tricycle().getSpeed());
        Judge.eq("incr", 6, () -> { Tricycle t = new Tricycle(); t.incr(); return t.getSpeed(); });
        Judge.eq("brake", 4, () -> { Tricycle t = new Tricycle(); t.brake(); return t.getSpeed(); });
        Judge.eq("setSpeed", 42, () -> { Tricycle t = new Tricycle(); t.setSpeed(42); return t.getSpeed(); });
        Judge.eq("copy constructor copies the speed", 9, () -> { Tricycle a = new Tricycle(); a.setSpeed(9); return new Tricycle(a).getSpeed(); });
        Judge.eq("copy is independent of the original", "6 5", () -> { Tricycle a = new Tricycle(); Tricycle b = new Tricycle(a); a.incr(); return a.getSpeed() + " " + b.getSpeed(); });
        Judge.eq("full driver, input 12", "5 6 6 7 12 5 11", () -> {
            Tricycle t1 = new Tricycle(); String r = t1.getSpeed() + ""; t1.incr(); r += " " + t1.getSpeed();
            Tricycle t2 = new Tricycle(t1); r += " " + t2.getSpeed(); t2.incr(); r += " " + t2.getSpeed();
            t2.setSpeed(12); r += " " + t2.getSpeed(); t1.brake(); t2.brake(); return r + " " + t1.getSpeed() + " " + t2.getSpeed(); });
        Judge.end();
    }
}
