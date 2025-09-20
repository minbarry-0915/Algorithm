import java.util.*;

class Item{
    int x;
    int y;
    int count;
    
    Item(int x, int y, int count){
        this.x = x;
        this.y = y;
        this.count = count;
    }
}

class Solution {
    int[] dx = {-1,1,0,0};
    int[] dy = {0,0,-1,1};
    public int solution(int[][] maps) {
        int result = bfs(maps);
        return result;
    }
    
    int bfs(int[][] maps){
        int n = maps.length;
        int m = maps[0].length;
        
        Deque<Item> queue = new ArrayDeque<>();
        queue.offerFirst(new Item(0,0,1));
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        
        while (!queue.isEmpty()){
            Item curr = queue.pollFirst();
            int x = curr.x;
            int y = curr.y;
            int count = curr.count;
            
            if (x == n - 1 && y == m - 1){
                return count;
            }
            
            for (int d = 0; d < 4; d++){
                int nx = x + dx[d];
                int ny = y + dy[d];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx][ny] == 1 && !visited[nx][ny]){
                    visited[nx][ny] = true;
                    queue.offerLast(new Item(nx,ny,count + 1));
                }
            }
        }
        return -1;
    }
}