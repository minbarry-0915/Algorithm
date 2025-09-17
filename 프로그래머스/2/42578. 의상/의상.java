import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> closet = new HashMap<>();
        
        for (String[] cloth: clothes){
            String type = cloth[1];
            closet.put(type, closet.getOrDefault(type,0) + 1);
        }
        
        int answer = 1;
        for (int count: closet.values()){
            answer *= (count + 1);
        }
        
        return answer - 1;
    }
}