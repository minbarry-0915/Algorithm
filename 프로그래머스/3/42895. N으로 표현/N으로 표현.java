import java.util.*;
class Solution {
    public int solution(int N, int number) {
        if (N == number) return 1;
        
        List<Set<Integer>> dp = new ArrayList<>();
        for (int i = 0; i <= 8; i++){
            dp.add(new HashSet<>());
        }
        
        for (int i = 1; i <= 8; i++){
            // 숫자 이어붙기
            int repeated = Integer.parseInt(String.valueOf(N).repeat(i));
            if (repeated > 0 && repeated <= 32000) dp.get(i).add(repeated);
            
            // 이전 dp 집합 조합
            for (int j = 1; j < i; j++){
                for (int x : dp.get(j)){
                    for (int y : dp.get(i - j)){
                        int[] candidates = {x + y, x - y, y - x, x * y};
                        for (int c : candidates){
                            if (c > 0 && c <= 32000) dp.get(i).add(c);
                        }
                        // 나누기 연산 (0 방지, 범위 체크)
                        if (y != 0){
                            int div1 = x / y;
                            if (div1 > 0 && div1 <= 32000) dp.get(i).add(div1);
                        }
                        if (x != 0){
                            int div2 = y / x;
                            if (div2 > 0 && div2 <= 32000) dp.get(i).add(div2);
                        }
                    }
                }
            }
            
            // 목표 숫자 확인
            if (dp.get(i).contains(number)) return i;
        }
        
        return -1; // 8번 초과 시 불가능
    }
}