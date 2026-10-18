import java.util.Scanner;

class Employee {
    private int e_Id;
    private String name;
    private int[] salary = new int[6];

    public void getValues(int id, String name, int[] salary) { e_Id = id; this.name = name; this.salary = salary.clone(); }

    public void printValues() {
        System.out.println(e_Id); System.out.println(name);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 6; i++) { if (i > 0) sb.append(' '); sb.append(salary[i]); }
        System.out.println(sb);
    }

    public int calTotalSalary() { int s = 0; for (int x : salary) s += x; return s; }

    public int maxSalary() { int m = 0; for (int i = 1; i < 6; i++) if (salary[i] > salary[m]) m = i; return m + 1; }
}
