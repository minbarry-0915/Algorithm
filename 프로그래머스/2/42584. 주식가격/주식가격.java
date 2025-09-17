import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        Deque<Integer> queue = new ArrayDeque<>();
        Deque<Integer> answer = new ArrayDeque<>();
        
        for (int i = 0; i < prices.length; i++) {
            queue.offerLast(i);
        }
        
        while (!queue.isEmpty()){
            int idx = queue.pollFirst();
            int curr = prices[idx];
            
            int time = 0;
            for (int i = idx + 1; i < prices.length; i ++){
                time ++;
                if (prices[i] < curr) break;
            }
            answer.offerLast(time);
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}