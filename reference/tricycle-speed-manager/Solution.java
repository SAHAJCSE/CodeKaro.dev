import java.util.Scanner;

class Tricycle {
    private int speed;
    public Tricycle() { speed = 5; }
    public Tricycle(Tricycle t) { speed = t.speed; }
    public void setSpeed(int s) { speed = s; }
    public int getSpeed() { return speed; }
    public void incr() { speed++; }
    public void brake() { speed--; }
}
