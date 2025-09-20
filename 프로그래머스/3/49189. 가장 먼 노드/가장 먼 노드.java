import java.util.*;

class Item{
    int x;
    int dist;
    
    Item(int x, int dist){
        this.x = x;
        this.dist = dist;
    }
}

class Solution {
    public int solution(int n, int[][] edge) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 1; i < n + 1; i ++){
            graph.put(i, new ArrayList<>());
        }
        
        for (int i = 0; i < edge.length; i++){
            int a = edge[i][0];
            int b = edge[i][1];
            
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
    
        Deque<Integer> queue = new ArrayDeque<>();
        int[] visited = new int[n + 1];
        for (int i = 0; i < n + 1; i ++){
            visited[i] = -1;
        }
        queue.offerLast(1);
        visited[1] = 0;
        
        while (!queue.isEmpty()){
            int curr = queue.pollFirst();
            
            for (int next: graph.get(curr)){
                if (visited[next] == -1){
                    visited[next] = visited[curr] + 1;
                    queue.offerLast(next);
                }
            }
        }
        
        int mx = 0;
        int count = 0;
        for (int v: visited){
            if (mx < v){
                mx = v;
                count = 1;
            }else if(mx == v){
                count ++;
            }
        }
        return count;
    }
}