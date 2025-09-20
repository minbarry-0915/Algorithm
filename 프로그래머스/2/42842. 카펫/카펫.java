class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        int total = brown + yellow;
        for (int h = 3; h <= total; h ++){
           if (total % h != 0) continue; // 약수인지 확인
            int w = total / h;
            
            if (w >= h && ((w - 2) * (h - 2) == yellow)){
                answer = new int[]{w,h};
            }
        }
        
        return answer;
    }
}