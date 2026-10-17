import java.util.*;

class Result {
    static int maxMarks(int[] marks, int N) {
        int best = marks[0];
        for (int i = 1; i < N; i++) best = Math.max(best, marks[i]);
        return best;
    }
}
