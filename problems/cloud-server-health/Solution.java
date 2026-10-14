import java.util.*;

class Main {
    public static ArrayList<Integer>
    findOverloadedServers(ArrayList<Integer> cpuUsage) {
        // Write your code here
ArrayList<Integer> num=new ArrayList<>();
for(int id:cpuUsage){
if(id>=80){
num.add(id);
}
}
return num;

       
    }
}
