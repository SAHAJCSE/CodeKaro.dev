import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Class Student");
        Judge.out("printValues (sample)", "14\nDeepak Singh\n57 85 45 86 95\n", () -> new Student(14, "Deepak Singh", new int[]{57,85,45,86,95}).printValues());
        Judge.eq("calTotalMarks (sample)", 368, () -> new Student(14, "Deepak Singh", new int[]{57,85,45,86,95}).calTotalMarks());
        Judge.eq("secondMaxMarks (sample)", 86, () -> new Student(14, "Deepak Singh", new int[]{57,85,45,86,95}).secondMaxMarks());
        Judge.eq("sorted descending", 99, () -> new Student(1, "A", new int[]{100,99,98,97,96}).secondMaxMarks());
        Judge.eq("sorted ascending", 40, () -> new Student(2, "B", new int[]{10,20,30,40,50}).secondMaxMarks());
        Judge.eq("highest in the middle", 90, () -> new Student(3, "C", new int[]{10,100,90,20,30}).secondMaxMarks());
        Judge.eq("total of all 100s", 500, () -> new Student(4, "D E", new int[]{100,100,100,100,100}).calTotalMarks());
        Judge.out("name with spaces", "9\nA B C\n1 2 3 4 5\n", () -> new Student(9, "A B C", new int[]{1,2,3,4,5}).printValues());
        Judge.end();
    }
}
