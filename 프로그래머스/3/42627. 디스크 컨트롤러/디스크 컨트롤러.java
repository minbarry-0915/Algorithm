import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int n = jobs.length;
        
        Arrays.sort(jobs, (a,b) -> a[0] - b[0]);
        PriorityQueue<int[]> queue = new PriorityQueue<>((a,b) -> {
            if (a[1] == b[1]) return Integer.compare(a[2],b[2]);
            return Integer.compare(a[1],b[1]);
        });
        
        
        int time = 0; // 현재 시간
        int idx = 0; // 남은 작업 시작지점
        int total = 0; // 총 반환시간
        
        while (idx < n || !queue.isEmpty()){
            // 시간 내에 요청 들어온 작업들 대기 큐에 넣음
            while (idx < n && jobs[idx][0] <= time){
                queue.add(new int[]{jobs[idx][0], jobs[idx][1], idx});
                idx += 1;
            }
            
            // 대기 큐에 들어읶던 작업처리 
            // 대기 큐에 아무것도 없으면 다음 작업의 요청시간으로 점프
            if (queue.isEmpty()){
                time = jobs[idx][0];
            } else{
                int[] job = queue.poll();
                time += job[1]; // 소요시간 더하기
                total += time - job[0]; // 반환시간 = 현재시간 - 요청시간 더하기
            }
        }
        return total / n;
    }
}