import java.util.*;

class Solution {
    Set<Integer> numbers = new HashSet<>();
    
    public int solution(String numbersStr) {
        boolean[] visited = new boolean[numbersStr.length()];
        dfs("", numbersStr, visited);
        
        int count = 0;
        for (int num: numbers){
            if(isPrime(num)) count ++;
        }
        
        return count;
    }
    
    void dfs(String current, String numbersStr, boolean[] visited){
        if (!current.equals("")){
            numbers.add(Integer.parseInt(current));
        }
        
        for (int i = 0; i < numbersStr.length(); i ++){
            if (!visited[i]){
                visited[i] = true;
                dfs(current + numbersStr.charAt(i), numbersStr, visited);
                visited[i] = false;
            }
        }
    }
    
    boolean isPrime(int n){
        if (n < 2) return false;
        
        for (int i = 2; i * i <= n; i++){
            if (n % i == 0) return false;
        }
        return true;
    }
}