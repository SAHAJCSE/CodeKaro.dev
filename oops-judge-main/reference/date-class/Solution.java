class Date {
    private int month, date;
    private static final int[] D = {31,28,31,30,31,30,31,31,30,31,30,31};
    public Date() { month = 1; date = 1; }
    public Date(int month, int date) { this.month = month; this.date = date; }
    public int getMonth() { return month; }
    public int getDay() { return date; }
    public int daysInMonth() { return D[month - 1]; }
    public void nextDay() {
        if (date < daysInMonth()) date++;
        else { date = 1; month = month == 12 ? 1 : month + 1; }
    }
}
