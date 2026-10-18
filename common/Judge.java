import java.io.*;
import java.util.*;
import java.util.concurrent.*;

/** Tiny LeetCode-style judge: runs your code against test cases with a time limit. */
public final class Judge {
    public interface Body { void run() throws Exception; }
    public interface Fn { Object call() throws Exception; }

    private static final long TIMEOUT_MS = 2000;
    private static final int MAX_OUTPUT_BYTES = 64 * 1024;
    private static final PrintStream REAL_OUT = System.out;
    private static final InputStream REAL_IN = System.in;
    private static final InputStream EMPTY_IN = new ByteArrayInputStream(new byte[0]);

    private static int total = 0;
    private static int passed = 0;
    private static String title = "";
    private static String marker = "";
    private static volatile boolean finished = false;

    public static final class TestCaseRecord {
        public int index;
        public String name;
        public boolean passed;
        public String status; // "PASSED", "FAILED", "TIME_LIMIT_EXCEEDED", "RUNTIME_ERROR"
        public String expected;
        public String actual;
        public String stdout;
        public long runtimeMs;
        public boolean sample;
    }

    private static final List<TestCaseRecord> testRecords = new ArrayList<>();

    static {
        // Securely read result marker from stdin once at startup before any user code runs
        try {
            if (REAL_IN.available() > 0) {
                BufferedReader reader = new BufferedReader(new InputStreamReader(REAL_IN, java.nio.charset.StandardCharsets.UTF_8));
                String line = reader.readLine();
                if (line != null) {
                    marker = line.trim();
                }
            }
        } catch (Throwable t) {
            marker = "";
        }
        // Immediately replace System.in with an empty stream so user code cannot read from it
        System.setIn(EMPTY_IN);

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            if (!finished) {
                try {
                    printJsonLine();
                } catch (Throwable ignored) {}
            }
        }));
    }

    public static void begin(String t) {
        title = t;
        total = 0;
        passed = 0;
        finished = false;
        testRecords.clear();
        REAL_OUT.println("\n=== " + t + " ===");
    }

    public static void begin(String t, String... args) {
        begin(t);
    }

    /** Compare the returned value of a function with the expected value. */
    public static void eq(String name, Object expected, Fn f) {
        Object[] box = new Object[1];
        Res r = execute(() -> box[0] = f.call(), null);
        boolean ok = r.err == null && !r.tle && same(expected, box[0]);
        report(name, r, ok, show(expected), show(box[0]));
    }

    /** Compare what a method prints (no stdin). */
    public static void out(String name, String expected, Body b) {
        io(name, null, expected, b);
    }

    /** Feed stdin, run the body, compare what was printed. */
    public static void io(String name, String stdin, String expected, Body b) {
        Res r = execute(b, stdin);
        String exp = norm(expected);
        String act = norm(r.out);
        report(name, r, r.err == null && !r.tle && exp.equals(act), block(exp), block(act));
    }

    public static void end() {
        finished = true;
        boolean ok = (total > 0) && (passed == total);
        REAL_OUT.println("-----------------------------------------");
        REAL_OUT.println(ok ? "Result: " + passed + "/" + total + " passed  ->  ACCEPTED"
                            : "Result: " + passed + "/" + total + " passed  ->  WRONG ANSWER");
        printJsonLine();
        REAL_OUT.flush();
        System.exit(ok ? 0 : 1);
    }

    // ---------------------------------------------------------------- internals
    private static final class Res {
        String out = "";
        Throwable err;
        boolean tle;
        long timeMs;
    }

    private static class BoundedOutputStream extends OutputStream {
        private final ByteArrayOutputStream bos = new ByteArrayOutputStream();
        private boolean truncated = false;

        @Override
        public void write(int b) {
            if (bos.size() < MAX_OUTPUT_BYTES) {
                bos.write(b);
            } else if (!truncated) {
                truncated = true;
                try {
                    bos.write("\n[output truncated]".getBytes(java.nio.charset.StandardCharsets.UTF_8));
                } catch (IOException ignored) {}
            }
        }

        @Override
        public void write(byte[] b, int off, int len) {
            if (bos.size() + len <= MAX_OUTPUT_BYTES) {
                bos.write(b, off, len);
            } else if (bos.size() < MAX_OUTPUT_BYTES) {
                int take = MAX_OUTPUT_BYTES - bos.size();
                bos.write(b, off, take);
                if (!truncated) {
                    truncated = true;
                    try {
                        bos.write("\n[output truncated]".getBytes(java.nio.charset.StandardCharsets.UTF_8));
                    } catch (IOException ignored) {}
                }
            } else if (!truncated) {
                truncated = true;
                try {
                    bos.write("\n[output truncated]".getBytes(java.nio.charset.StandardCharsets.UTF_8));
                } catch (IOException ignored) {}
            }
        }

        @Override
        public String toString() {
            return bos.toString(java.nio.charset.StandardCharsets.UTF_8);
        }
    }

    private static Res execute(Body b, String stdin) {
        Res res = new Res();
        BoundedOutputStream bos = new BoundedOutputStream();
        PrintStream cap = new PrintStream(bos, true, java.nio.charset.StandardCharsets.UTF_8);
        System.setOut(cap);
        if (stdin != null) {
            System.setIn(new ByteArrayInputStream(stdin.getBytes(java.nio.charset.StandardCharsets.UTF_8)));
        } else {
            System.setIn(EMPTY_IN);
        }

        ExecutorService ex = Executors.newSingleThreadExecutor(r -> {
            Thread t = new Thread(null, r, "solution", 64L << 20);
            t.setDaemon(true);
            return t;
        });

        long start = System.currentTimeMillis();
        try {
            Future<Object> f = ex.submit((Callable<Object>) () -> { b.run(); return null; });
            f.get(TIMEOUT_MS, TimeUnit.MILLISECONDS);
        } catch (TimeoutException e) {
            res.tle = true;
        } catch (ExecutionException e) {
            res.err = e.getCause();
        } catch (Throwable e) {
            res.err = e;
        } finally {
            res.timeMs = System.currentTimeMillis() - start;
            ex.shutdownNow();
            cap.flush();
            System.setOut(REAL_OUT);
            System.setIn(EMPTY_IN);
            res.out = bos.toString();
        }
        return res;
    }

    private static void report(String name, Res r, boolean ok, String exp, String act) {
        int idx = total;
        total++;

        TestCaseRecord rec = new TestCaseRecord();
        rec.index = idx;
        rec.name = name;
        rec.passed = ok;
        rec.expected = exp;
        rec.actual = act;
        rec.stdout = r.out;
        rec.runtimeMs = r.timeMs;
        rec.sample = (idx < 3);

        if (ok) {
            passed++;
            rec.status = "PASSED";
            testRecords.add(rec);
            REAL_OUT.println("[PASS] " + name);
            return;
        }

        REAL_OUT.println("[FAIL] " + name);
        if (r.tle) {
            REAL_OUT.println("       Time Limit Exceeded (> " + TIMEOUT_MS + " ms)");
            rec.status = "TIME_LIMIT_EXCEEDED";
            rec.actual = "Time Limit Exceeded (> " + TIMEOUT_MS + " ms)";
            testRecords.add(rec);
            flushAndHaltOnTle();
            return;
        }

        if (r.err != null) {
            rec.status = "RUNTIME_ERROR";
            String errStr = "Runtime Error: " + r.err;
            REAL_OUT.println("       " + errStr);
            String trace = "";
            for (StackTraceElement s : r.err.getStackTrace()) {
                String c = s.getClassName();
                if (!c.startsWith("Judge") && !c.equals("Test") && !c.startsWith("java.") && !c.startsWith("jdk.")) {
                    trace = "at " + s;
                    REAL_OUT.println("       " + trace);
                    break;
                }
            }
            rec.actual = trace.isEmpty() ? errStr : errStr + " (" + trace + ")";
            testRecords.add(rec);
            return;
        }

        rec.status = "FAILED";
        REAL_OUT.println("       Expected: " + exp);
        REAL_OUT.println("       Actual  : " + act);
        testRecords.add(rec);
    }

    private static void flushAndHaltOnTle() {
        finished = true;
        REAL_OUT.println("-----------------------------------------");
        REAL_OUT.println("Result: " + passed + "/" + total + " passed  ->  TIME LIMIT EXCEEDED");
        printJsonLine();
        REAL_OUT.flush();
        // Force immediate shutdown so infinite CPU-bound threads do not delay exit
        Runtime.getRuntime().halt(1);
    }

    private static void printJsonLine() {
        if (marker == null || marker.isEmpty()) {
            return;
        }
        StringBuilder sb = new StringBuilder(marker);
        sb.append("{\"tests\":[");
        for (int i = 0; i < testRecords.size(); i++) {
            if (i > 0) sb.append(",");
            TestCaseRecord rec = testRecords.get(i);
            sb.append("{");
            sb.append("\"index\":").append(rec.index).append(",");
            sb.append("\"name\":").append(quoteJson(rec.name)).append(",");
            sb.append("\"passed\":").append(rec.passed).append(",");
            sb.append("\"status\":").append(quoteJson(rec.status)).append(",");
            sb.append("\"expected\":").append(rec.expected == null ? "null" : quoteJson(rec.expected)).append(",");
            sb.append("\"actual\":").append(rec.actual == null ? "null" : quoteJson(rec.actual)).append(",");
            sb.append("\"stdout\":").append(quoteJson(rec.stdout)).append(",");
            sb.append("\"runtimeMs\":").append(rec.runtimeMs).append(",");
            sb.append("\"sample\":").append(rec.sample);
            sb.append("}");
        }
        sb.append("]}");
        REAL_OUT.println(sb.toString());
        REAL_OUT.flush();
    }

    private static String quoteJson(String s) {
        if (s == null) return "null";
        StringBuilder sb = new StringBuilder("\"");
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            switch (c) {
                case '"':  sb.append("\\\""); break;
                case '\\': sb.append("\\\\"); break;
                case '\b': sb.append("\\b");  break;
                case '\f': sb.append("\\f");  break;
                case '\n': sb.append("\\n");  break;
                case '\r': sb.append("\\r");  break;
                case '\t': sb.append("\\t");  break;
                default:
                    if (c < 0x20 || c > 0x7E) {
                        sb.append(String.format("\\u%04x", (int) c));
                    } else {
                        sb.append(c);
                    }
            }
        }
        sb.append("\"");
        return sb.toString();
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
        if (s == null) return "";
        String[] lines = s.replace("\r", "").split("\n", -1);
        int n = lines.length;
        for (int i = 0; i < n; i++) lines[i] = lines[i].replaceAll("\\s+$", "");
        while (n > 0 && lines[n - 1].isEmpty()) n--;
        return String.join("\n", Arrays.copyOf(lines, n));
    }

    private static String block(String s) {
        if (s == null) return "(nothing printed)";
        if (s.length() > 300) s = s.substring(0, 300) + "...";
        return s.isEmpty() ? "(nothing printed)" : "\n         " + s.replace("\n", "\n         ");
    }

    private static String show(Object o) {
        if (o == null) return "null";
        if (o instanceof String) return "\"" + o + "\"";
        if (o instanceof int[]) return Arrays.toString((int[]) o);
        if (o instanceof long[]) return Arrays.toString((long[]) o);
        if (o instanceof char[]) return Arrays.toString((char[]) o);
        if (o instanceof boolean[]) return Arrays.toString((boolean[]) o);
        if (o instanceof Object[]) return Arrays.deepToString((Object[]) o);
        String s = String.valueOf(o);
        return s.length() > 300 ? s.substring(0, 300) + "..." : s;
    }
}
