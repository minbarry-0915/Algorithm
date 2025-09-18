import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] pattern1 = {1,2,3,4,5};
        int[] pattern2 = {2,1,2,3,2,4,2,5};
        int[] pattern3 = {3,3,1,1,2,2,4,4,5,5};
        
        int answer1 = 0;
        int answer2 = 0;
        int answer3 = 0;
        
        for (int i = 0; i < answers.length; i++) {
            if (pattern1[i % pattern1.length] == answers[i]) answer1++;
            if (pattern2[i % pattern2.length] == answers[i]) answer2++;
            if (pattern3[i % pattern3.length] == answers[i]) answer3++;
        }
        
        List<Integer> maxAnswers = Arrays.asList(answer1, answer2, answer3);
        int maxAnswer = Collections.max(maxAnswers);
        
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= 3; i++) {
            if (maxAnswers.get(i - 1) == maxAnswer) {
                result.add(i);
            }
        }
        return result.stream().mapToInt(i -> i).toArray();
    }
}