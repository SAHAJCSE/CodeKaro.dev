import java.io.*;
import java.util.*;
import java.util.concurrent.*;

/** Tiny LeetCode-style judge: runs your code against test cases with a time limit. */
public final class Judge {
    public interface Body { void run() throws Exception; }
    public interface Fn { Object call() throws Exception; }

    private static final long TIMEOUT_MS = 2000;
    private static int total, passed;
    private static String title;

    private static final class Res { String out = ""; Throwable err; boolean tle; }

    public static void begin(String t) {
        title = t; total = 0; passed = 0;
        System.out.println("\n=== " + t + " ===");
    }

    /** Compare the returned value of a function with the expected value. */
    public static void eq(String name, Object expected, Fn f) {
        Object[] box = new Object[1];
        Res r = execute(() -> box[0] = f.call(), null);
        boolean ok = r.err == null && !r.tle && same(expected, box[0]);
        report(name, r, ok, show(expected), show(box[0]));
    }

    /** Compare what a method prints (no stdin). */
    public static void out(String name, String expected, Body b) { io(name, null, expected, b); }

    /** Feed stdin, run the body, compare what was printed. */
    public static void io(String name, String stdin, String expected, Body b) {
        Res r = execute(b, stdin);
        String exp = norm(expected), act = norm(r.out);
        report(name, r, r.err == null && !r.tle && exp.equals(act), block(exp), block(act));
    }

    public static void end() {
        boolean ok = passed == total;
        System.out.println("-----------------------------------------");
        System.out.println(ok ? "Result: " + passed + "/" + total + " passed  ->  ACCEPTED"
                              : "Result: " + passed + "/" + total + " passed  ->  WRONG ANSWER");
        System.out.flush();
        System.exit(ok ? 0 : 1);
    }

    // ---------------------------------------------------------------- internals
    private static Res execute(Body b, String stdin) {
        Res res = new Res();
        PrintStream oldOut = System.out; InputStream oldIn = System.in;
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        PrintStream cap = new PrintStream(bos, true);
        System.setOut(cap);
        if (stdin != null) System.setIn(new ByteArrayInputStream(stdin.getBytes()));
        ExecutorService ex = Executors.newSingleThreadExecutor(r -> {
            Thread t = new Thread(null, r, "solution", 64L << 20); t.setDaemon(true); return t; });
        try {
            Future<Object> f = ex.submit((Callable<Object>) () -> { b.run(); return null; });
            f.get(TIMEOUT_MS, TimeUnit.MILLISECONDS);
        } catch (TimeoutException e) { res.tle = true; }
        catch (ExecutionException e) { res.err = e.getCause(); }
        catch (Exception e) { res.err = e; }
        finally {
            ex.shutdownNow(); cap.flush();
            System.setOut(oldOut); System.setIn(oldIn);
            res.out = bos.toString();
        }
        return res;
    }

    private static void report(String name, Res r, boolean ok, String exp, String act) {
        total++;
        if (ok) { passed++; System.out.println("[PASS] " + name); return; }
        System.out.println("[FAIL] " + name);
        if (r.tle) { System.out.println("       Time Limit Exceeded (> " + TIMEOUT_MS + " ms)"); return; }
        if (r.err != null) {
            System.out.println("       Runtime Error: " + r.err);
            for (StackTraceElement s : r.err.getStackTrace()) {
                String c = s.getClassName();
                if (!c.startsWith("Judge") && !c.equals("Test") && !c.startsWith("java.")
                        && !c.startsWith("jdk.")) { System.out.println("       at " + s); break; }
            }
            return;
        }
        System.out.println("       Expected: " + exp);
        System.out.println("       Actual  : " + act);
    }

    private static boolean same(Object a, Object b) {
        if (a instanceof Number && b instanceof Number) {
            if (a instanceof Double || a instanceof Float || b instanceof Double || b instanceof Float)
                return Math.abs(((Number) a).doubleValue() - ((Number) b).doubleValue()) < 1e-6;
            return ((Number) a).longValue() == ((Number) b).longValue();
        }
        return Objects.deepEquals(a, b);
    }

    private static String norm(String s) {
        String[] lines = s.replace("\r", "").split("\n", -1);
        int n = lines.length;
        for (int i = 0; i < n; i++) lines[i] = lines[i].replaceAll("\\s+$", "");
        while (n > 0 && lines[n - 1].isEmpty()) n--;
        return String.join("\n", Arrays.copyOf(lines, n));
    }

    private static String block(String s) {
        if (s.length() > 300) s = s.substring(0, 300) + "...";
        return s.isEmpty() ? "(nothing printed)" : "\n         " + s.replace("\n", "\n         ");
    }

    private static String show(Object o) {
        String s;
        if (o == null) s = "null";
        else if (o instanceof String) s = "\"" + o + "\"";
        else if (o instanceof int[]) s = Arrays.toString((int[]) o);
        else if (o instanceof long[]) s = Arrays.toString((long[]) o);
        else if (o instanceof char[]) s = Arrays.toString((char[]) o);
        else if (o instanceof boolean[]) s = Arrays.toString((boolean[]) o);
        else if (o instanceof Object[]) s = Arrays.deepToString((Object[]) o);
        else s = String.valueOf(o);
        return s.length() > 300 ? s.substring(0, 300) + "..." : s;
    }
}
