import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    public int solution(int bridge_length, int limit_weight, int[] truck_weights) {
        Deque<Integer> waiting = new ArrayDeque<>();
        Deque<Integer> bridge = new ArrayDeque<>();  
        int time = 0;
        int totalWeight = 0;
        
        for (int w: truck_weights){
            waiting.offerLast(w);
        }
        
        // 다리에 의미없는 값 채워주기
        for (int i = 0; i < bridge_length; i ++){
            bridge.offerLast(0);
        }

        // 다리가 빌 때까지 진행 : 모든 트럭이 다 지나갔다는 뜻임
        while (!bridge.isEmpty()){
            // 다리 상의 트럭 통과 처리
            int gone = bridge.pollFirst();
            totalWeight -= gone;
            
            // 대기 큐가 있으면, 한계 이내일 경우 다리에 트럭 올림
            if (!waiting.isEmpty()){
                if (totalWeight + waiting.peekFirst() <= limit_weight){
                    int truck = waiting.pollFirst();
                    bridge.offerLast(truck);
                    totalWeight += truck;
                }else{
                    bridge.offerLast(0);
                }
            }
            
            time += 1;
        }
        
        return time;
    }
}