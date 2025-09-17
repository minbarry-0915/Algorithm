import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        
        int prev = -1;
        for (int num : arr){
            if (num != prev){
                list.add(num);      
            }
            prev = num;
        }
        
        return list.stream().mapToInt(i -> i).toArray();
    }
}