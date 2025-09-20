import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long left = 1;
        long right = (long) Arrays.stream(times).max().getAsInt() * n;
        long min = 0;
        
        while (left <= right){
            long mid = (left + right) / 2;
            
            long available = 0;
            
            for (int time: times){
                available += (mid / time);
            }
            
            if (available >= n){
                // 충분한 경우
                min = mid;
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return min;
    }
}