import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Assignment44 - Analyze Sentence");
        Judge.eq("sample 1", "3", () -> Main.analyzeSentence("Java is powerful"));
        Judge.eq("sample 2 (digits)", "Invalid Sentence", () -> Main.analyzeSentence("Java is powerful123"));
        Judge.eq("single word", "1", () -> Main.analyzeSentence("Hello"));
        Judge.eq("ten words", "10", () -> Main.analyzeSentence("a b c d e f g h i j"));
        Judge.eq("digit inside a word", "Invalid Sentence", () -> Main.analyzeSentence("abc1 def"));
        Judge.eq("digit only", "Invalid Sentence", () -> Main.analyzeSentence("2024"));
        Judge.end();
    }
}
