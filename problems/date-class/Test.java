import java.util.*;

public class Test {

    public static void main(String[] args) throws Exception {
        Judge.begin("Implement the Date class");
        int[] D = {31,28,31,30,31,30,31,31,30,31,30,31};
        Judge.eq("default constructor", "1/1", () -> { Date d = new Date(); return d.getMonth() + "/" + d.getDay(); });
        Judge.eq("sample: daysInMonth(3)", 31, () -> new Date(3, 25).daysInMonth());
        Judge.eq("sample: getDay / getMonth", "25 3", () -> { Date d = new Date(3, 25); return d.getDay() + " " + d.getMonth(); });
        Judge.eq("sample: nextDay", "26 3", () -> { Date d = new Date(3, 25); d.nextDay(); return d.getDay() + " " + d.getMonth(); });
        Judge.eq("daysInMonth for all 12 months", Arrays.toString(D), () -> { int[] r = new int[12]; for (int m = 1; m <= 12; m++) r[m-1] = new Date(m, 1).daysInMonth(); return Arrays.toString(r); });
        Judge.eq("30-day month end: Apr 30 -> May 1", "1 5", () -> { Date d = new Date(4, 30); d.nextDay(); return d.getDay() + " " + d.getMonth(); });
        Judge.eq("Feb 28 -> Mar 1", "1 3", () -> { Date d = new Date(2, 28); d.nextDay(); return d.getDay() + " " + d.getMonth(); });
        Judge.eq("Jan 31 -> Feb 1", "1 2", () -> { Date d = new Date(1, 31); d.nextDay(); return d.getDay() + " " + d.getMonth(); });
        Judge.eq("Dec 31 wraps to Jan 1", "1 1", () -> { Date d = new Date(12, 31); d.nextDay(); return d.getDay() + " " + d.getMonth(); });
        Judge.eq("365 nextDay() calls return to Jan 1", "1/1", () -> { Date d = new Date(); for (int i = 0; i < 365; i++) d.nextDay(); return d.getMonth() + "/" + d.getDay(); });
        Judge.eq("day 200 of the year is Jul 19", "7/19", () -> { Date d = new Date(); for (int i = 1; i < 200; i++) d.nextDay(); return d.getMonth() + "/" + d.getDay(); });
        Judge.end();
    }
}
