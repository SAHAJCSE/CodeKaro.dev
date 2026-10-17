import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Student Marks Management System");
        int[] a = {10,20,30,40,50};
        Judge.eq("sample: index 2", "30", () -> Main.getElement(a, 2));
        Judge.eq("sample: index 7", "Invalid Index", () -> Main.getElement(a, 7));
        Judge.eq("first element", "10", () -> Main.getElement(a, 0));
        Judge.eq("last element", "50", () -> Main.getElement(a, 4));
        Judge.eq("index == length", "Invalid Index", () -> Main.getElement(a, 5));
        Judge.eq("negative index", "Invalid Index", () -> Main.getElement(a, -1));
        Judge.eq("negative element value", "-9", () -> Main.getElement(new int[]{-9}, 0));
        Judge.end();
    }
}
