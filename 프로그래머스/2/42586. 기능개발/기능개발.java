import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        // 배열을 돌면서 각 작업당 작업일수 계산
        // 작업일수 가지고 돌면서 현재값이 이전 값보다 크면 count 푸시하고 초기화
        // 작거나 같으면 같이 배포임 count + 1
        
        List<Integer> workingDaysList = new ArrayList<>();
        int n = progresses.length;
        
        for (int i = 0; i < n ; i ++){
            int remain = 100 - progresses[i];
            int days = (remain + speeds[i] - 1) / speeds[i]; // 올림
            workingDaysList.add(days);
        }
        
        List<Integer> answer = new ArrayList<>();
        int count = 1;
        int prev = workingDaysList.get(0);

        
        for (int i = 1; i < n; i ++){
            int curr = workingDaysList.get(i);
            if (curr > prev){
                answer.add(count);
                count = 1;
                prev = curr;
            }else{
                count += 1;
            }
        }
        
        answer.add(count);
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}