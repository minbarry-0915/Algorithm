import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String,Integer> map = new HashMap<>();
        
        // 참가자 등록
        for (String p: participant){
            map.put(p, map.getOrDefault(p,0) + 1);
        }
        
        // 완주자 차감
        for (String c: completion){
            map.put(c, map.get(c) - 1);
        }
        
        // 0이 아닌 사람 찾기
        String answer = "";
        for (String key: map.keySet()){
            if (map.get(key) != 0){
                answer = key;
            }
        }
        return answer;
    }
}