import java.util.*;

class Main {
    public static ArrayList<Integer> updateInventory(ArrayList<Integer> books, int[] newBooks) {
        for (int b : newBooks) if (!books.contains(b)) books.add(b);
        return books;
    }
}
