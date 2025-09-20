import java.util.*; 
class Solution {
    public int solution(int distance, int[] rocks, int n) {
        Arrays.sort(rocks);
        
        int left = 1;
        int right = distance;
        int answer = 0;
        
        while(left <= right){
            int mid = (left + right) / 2;
            int removeRocks = 0;
            int prev = 0;
            
            for (int rock : rocks){
                if (rock - prev < mid){
                    removeRocks ++;
                }else{
                    prev = rock;
                }
            }
            
            // 마지막 돌 계산
            if(distance - prev < mid) removeRocks ++;
            
            if (removeRocks > n){
                right = mid - 1;
            }else{
                answer = mid;
                left = mid + 1;
            }
        }
        return answer;
    }
}