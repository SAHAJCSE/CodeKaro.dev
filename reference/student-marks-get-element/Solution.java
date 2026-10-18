import java.util.*;

class Main {
    public static String getElement(int arr[], int index)
    {
        try {
            return String.valueOf(arr[index]);
        } catch (ArrayIndexOutOfBoundsException e) {
            return "Invalid Index";
        }
    }
}
