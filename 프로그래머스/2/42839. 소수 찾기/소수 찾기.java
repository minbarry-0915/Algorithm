import java.util.*;

class Solution {
    Set<Integer> numbers = new HashSet<>();
    
    public int solution(String numbersStr) {
        // dfs 돌려서 경우의 수 set 저장
        // 소수인것만 골라서 계산
        int n = numbersStr.length();
        boolean[] visited = new boolean[n];
        dfs("", visited, numbersStr, n);
        int result = 0;
        
        for (int num: numbers){
            if (isPrime(num)) result ++;
        }
        return result;
    }
    
    void dfs(String current, boolean[] visited, String numbersStr, int n){
        if (current != ""){
            numbers.add(Integer.parseInt(current));
        }
        
        for (int i = 0; i < n; i++){
            if (!visited[i]){
                visited[i] = true;
                dfs(current + numbersStr.charAt(i), visited, numbersStr, n);
                visited[i] = false;
            }
        }
        return;
    }

    boolean isPrime(int x){
        if (x < 2) return false;
        
        for (int i = 2; i * i <= x; i ++){
            if (x % i == 0) return false;
        }
        return true;
    }
}