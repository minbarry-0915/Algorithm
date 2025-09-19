import java.io.*;
import java.util.Deque;
import java.util.ArrayDeque;

class Point {
    int x,y;
    Point (int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[][] grid = new String[n][n];

        for (int i = 0; i < n; i++){
            String s = br.readLine();
            for (int j = 0; j < n; j ++){
                grid[i][j] = String.valueOf(s.charAt(j));
            }
        }

        boolean[][] visited = new boolean[n][n];
        boolean[][] visited2 = new boolean[n][n];

        int count1 = 0;
        int count2 = 0;

        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j ++) {
                if (!visited[i][j]) {
                    count1 += bfs(i, j, grid, visited, false, n);
                }
                if (!visited2[i][j]){
                    count2 += bfs(i,j,grid, visited2, true, n);
                }
            }
        }

        System.out.println(count1 + " " + count2);
    }

    static int bfs(int i, int j, String[][]grid, boolean[][] visited, boolean isBlind, int n){
        Deque<Point> queue = new ArrayDeque<>();
        queue.offerLast(new Point(i,j));
        visited[i][j] = true;
        String color = grid[i][j];

        while (!queue.isEmpty()){
            Point p = queue.pollFirst();
            int x = p.x;
            int y = p.y;

            for (int d = 0; d < 4; d ++){
                int nx = x + dx[d];
                int ny = y + dy[d];
                // 범위내, 미방문, 컬러 구분
                 if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                    if (!isBlind) {
                        // 정상인
                        if (grid[nx][ny].equals(color)) {
                            visited[nx][ny] = true;
                            queue.offerLast(new Point(nx, ny));
                        }
                    } else {
                        // 적록색약
                        if (color.equals(grid[nx][ny]) ||
                            (color.equals("R") && grid[nx][ny].equals("G")) ||
                            (color.equals("G") && grid[nx][ny].equals("R"))) {
                            visited[nx][ny] = true;
                            queue.offerLast(new Point(nx, ny));
                        }
                    }
                }
            }
        }
        return 1;
    }


}