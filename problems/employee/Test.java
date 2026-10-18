import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Employee");
        int[] s = {12313, 12001, 10333, 14923, 15783, 10010};
        Judge.out("printValues (sample)", "3234\nNitin Kumar\n12313 12001 10333 14923 15783 10010\n", () -> { Employee e = new Employee(); e.getValues(3234, "Nitin Kumar", s); e.printValues(); });
        Judge.eq("calTotalSalary (sample)", 75363, () -> { Employee e = new Employee(); e.getValues(3234, "Nitin Kumar", s); return e.calTotalSalary(); });
        Judge.eq("maxSalary (sample) -> month 5", 5, () -> { Employee e = new Employee(); e.getValues(3234, "Nitin Kumar", s); return e.maxSalary(); });
        Judge.eq("max in first month", 1, () -> { Employee e = new Employee(); e.getValues(1, "A", new int[]{99999,1,2,3,4,5}); return e.maxSalary(); });
        Judge.eq("max in last month", 6, () -> { Employee e = new Employee(); e.getValues(1, "A", new int[]{1,2,3,4,5,100000}); return e.maxSalary(); });
        Judge.eq("total of large salaries", 600000, () -> { Employee e = new Employee(); e.getValues(2, "B C", new int[]{100000,100000,100000,100000,100000,100000}); return e.calTotalSalary(); });
        Judge.out("printValues with a 3-word name", "7\nMary Ann Lee\n1 2 3 4 5 6\n", () -> { Employee e = new Employee(); e.getValues(7, "Mary Ann Lee", new int[]{1,2,3,4,5,6}); e.printValues(); });
        Judge.end();
    }
}
