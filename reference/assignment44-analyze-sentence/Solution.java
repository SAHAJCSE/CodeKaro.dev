import java.util.*;

class Main {
    public static String analyzeSentence(String sentence)
    {
        for (char c : sentence.toCharArray()) if (Character.isDigit(c)) return "Invalid Sentence";
        return String.valueOf(sentence.trim().split("\\s+").length);
    }
}
