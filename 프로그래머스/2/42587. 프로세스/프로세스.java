import java.util.Deque;
import java.util.ArrayDeque;

class Process {
    int priority;
    int index;
    
    Process(int priority, int index){
        this.priority = priority;
        this.index = index;
    }
}

class Solution {
    public int solution(int[] priorities, int location) {
        Deque<Process> queue = new ArrayDeque();
        int n = priorities.length;
        for (int i = 0; i < n; i ++){
            queue.offerLast(new Process(priorities[i], i));
        }
        
        int count = 0;
        
        while (!queue.isEmpty()){
            Process current = queue.pollFirst();
            boolean hasHigher = false;
            
            for (Process p: queue){
                if (p.priority > current.priority){
                    hasHigher = true;
                    break;
                }
            }
            
            if (hasHigher){
                queue.offerLast(current);
            }else{
                count ++;
                if (current.index == location){
                    return count;
                }
            }
        }
        
        return count;
    }
}