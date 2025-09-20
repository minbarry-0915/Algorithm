import java.util.*;

class Solution {
    int count = 0;
    public int solution(int[] numbers, int target) {
        int n = numbers.length;
        dfs(numbers, target, 0, 0);
        return count;
    }
    
    void dfs(int[] numbers, int target, int total, int depth){
        if (depth == numbers.length){
            if(total == target){
                count += 1;
            }
            return;
        }
        
        dfs(numbers, target, total + numbers[depth], depth + 1);
        dfs(numbers, target, total - numbers[depth], depth + 1);
        
        return;
    }   
}