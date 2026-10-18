import java.util.Scanner;

class Main {
    static void strcat(char[] result, char[] str1, char[] str2) {
        int k = 0;
        for (char c : str1) result[k++] = c;
        for (char c : str2) result[k++] = c;
    }
}
