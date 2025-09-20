import java.util.*;

class Solution {
    String[] words = {"A", "E", "I", "O", "U"};
    Set<String> dictionary = new HashSet<>();

    public int solution(String word) {
        // DFS로 모든 단어 생성
        dfs("");

        // Set → List로 변환
        List<String> dictList = new ArrayList<>(dictionary);

        // 정렬: 사전 순, 길이 순
        Collections.sort(dictList, (a, b) -> {
            int cmp = a.compareTo(b);      // 알파벳 순
            if (cmp == 0) return a.length() - b.length(); // 길이 순
            return cmp;
        });

        // indexOf로 위치 찾기 (0-based)
        return dictList.indexOf(word) + 1;
    }

    void dfs(String current) {
        if (current.length() >= 1 && current.length() <= 5) {
            dictionary.add(current);
        }
        if (current.length() == 5) return;

        for (String w : words) {
            dfs(current + w);
        }
    }
}