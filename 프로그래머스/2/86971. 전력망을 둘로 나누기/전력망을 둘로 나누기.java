import java.util.*;
class Solution {
    public int solution(int n, int[][] wires) {
        // 그래프 초기화
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 1; i <= n; i++){
            graph.put(i, new ArrayList<>());
        }
        
        // 그래프 입력
        for (int[] wire: wires){
            int a = wire[0];
            int b = wire[1];
            
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        
        // 하나씩 끊어보기
        int answer = Integer.MAX_VALUE;
        for (int[]wire: wires){
            int a= wire[0];
            int b = wire[1];
            int count1 = bfs(a, graph, new int[]{a,b}, n);
            int count2 = n - count1;
            int diff = Math.abs(count1 - count2);
            answer = Math.min(answer,diff);
        }
        
        return answer;
    }
    
    int bfs(int start, Map<Integer, List<Integer>> graph, int[] cuttingEdge, int n){
        Deque <Integer> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[n + 1];
        int count = 1;
        
        queue.offerLast(start);
        visited[start] = true;
        
        while (!queue.isEmpty()){
            int curr = queue.pollFirst();
            
            for (int next : graph.get(curr)){
                if (!visited[next] && 
                    !(Arrays.equals(cuttingEdge, new int[]{curr, next}) || Arrays.equals(cuttingEdge, new int[]{next, curr}))) {
                    visited[next] = true;
                    queue.offerLast(next);
                    count++;
                }
            }
        }
        return count;
    }
}