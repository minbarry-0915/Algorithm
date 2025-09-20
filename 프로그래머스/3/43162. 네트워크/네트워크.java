import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        
        for (int i = 0; i < n; i ++){
            graph.put(i, new ArrayList<>());
        }
        
        for (int i = 0; i < n; i ++){
            for (int j = 0; j < n; j ++){
                if (i == j) continue;
                if (computers[i][j] == 1){
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }
        
        int count = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i ++){
            if(!visited[i]){
                count += bfs(i, graph, visited);
            }
        }
        return count;
    }
    
    int bfs(int start, Map<Integer, List<Integer>> graph, boolean[] visited){
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offerLast(start);
        visited[start] = true;
        
        while (!queue.isEmpty()){
            int curr = queue.pollFirst();
            
            for (int next: graph.get(curr)){
                if(!visited[next]){
                    visited[next] = true;
                    queue.offerLast(next);
                }
            }
        }
        
        return 1;
    }
}