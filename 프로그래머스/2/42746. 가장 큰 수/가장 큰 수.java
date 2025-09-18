import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        List<String> nums = new ArrayList<>();
        for (int n : numbers){
            nums.add(String.valueOf(n));
        }
        
        nums.sort((a,b) -> (b + a).compareTo(a + b));
        
        if (nums.get(0).equals("0")) return "0";
        
        StringBuilder sb = new StringBuilder();
        
        for (String n: nums){
            sb.append(n);
        }
        
        return sb.toString();
    }
}
