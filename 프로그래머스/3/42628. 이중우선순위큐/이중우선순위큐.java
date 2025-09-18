import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();        
        PriorityQueue<Integer> reversedHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        for (String op : operations){
            String[] parts = op.split(" ");
            String command = parts[0];
            int value = Integer.parseInt(parts[1]);
            
            if (command.equals("I")){
                heap.add(value);
                reversedHeap.add(value);    
            }else if (command.equals("D")){
                if (!heap.isEmpty()){
                   if (value == 1){
                        int mx = reversedHeap.poll();
                        heap.remove(mx);
                    }else{
                        int mn = heap.poll();
                        reversedHeap.remove(mn);
                    }
                }
            }
        }
        
        // 최댓값 최솟값 계산
        int[] answer = {0,0};
        
        if (!heap.isEmpty()){
            answer[0] = reversedHeap.poll();
            answer[1] = heap.poll();
        } 
        return answer;
    }
}