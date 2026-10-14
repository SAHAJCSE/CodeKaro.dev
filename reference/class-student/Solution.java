import java.util.*;

class Student {
    private int studentId;
    private String name;
    private int[] marks;

    public Student(int studentId, String name, int[] marks) { this.studentId = studentId; this.name = name; this.marks = marks.clone(); }

    public void printValues() {
        System.out.println(studentId); System.out.println(name);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < marks.length; i++) { if (i > 0) sb.append(' '); sb.append(marks[i]); }
        System.out.println(sb);
    }

    public int calTotalMarks() { int s = 0; for (int m : marks) s += m; return s; }

    public int secondMaxMarks() {
        int[] c = marks.clone(); Arrays.sort(c); return c[c.length - 2];
    }
}
