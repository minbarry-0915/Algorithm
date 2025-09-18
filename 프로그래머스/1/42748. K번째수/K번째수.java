import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> result = new ArrayList<>();
        
        for (int[] c : commands){
            int start = c[0] - 1; // 1based -> 0 based
            int end = c[1] - 1;
            int k = c[2] - 1;
            
            List<Integer> buffer = new ArrayList<>();
            for (int i = start; i <= end; i++){
                buffer.add(array[i]);
            }
            
            buffer.sort((a,b) -> a - b);
            result.add(buffer.get(k));
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}