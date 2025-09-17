import java.util.PriorityQueue;
import java.util.List;

class Solution {
    public int solution(int[] scoville, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int s : scoville){
            minHeap.add(s);
        }
        
        int count = 0;
        while (minHeap.size() > 1 && !checkAllSpicy(minHeap.peek(), k)){
            int first = minHeap.poll();
            int second = minHeap.poll();
            int mixed = first + (second * 2);
            minHeap.add(mixed);
            count ++;
        }
        return checkAllSpicy(minHeap.peek(), k) ? count : -1;
    }
    
    
    boolean checkAllSpicy(int first, int k){
        return first >= k;        
    }
}