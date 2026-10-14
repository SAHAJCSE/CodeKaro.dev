import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Search an element");
        int[] a = {3,10,20,4,7,4,5};
        Judge.eq("appears twice", 2, () -> Search.SearchElement(a, 4));
        Judge.eq("appears once", 1, () -> Search.SearchElement(a, 5));
        Judge.eq("not present", -1, () -> Search.SearchElement(a, 6));
        Judge.eq("first element", 1, () -> Search.SearchElement(a, 3));
        Judge.eq("all same", 7, () -> Search.SearchElement(new int[]{1,1,1,1,1,1,1}, 1));
        Judge.eq("negatives", 1, () -> Search.SearchElement(new int[]{-1,2,-3,4,-5,6,-7}, -5));
        Judge.eq("zero absent", -1, () -> Search.SearchElement(new int[]{-1,2,-3,4,-5,6,-7}, 0));
        Judge.end();
    }
}
