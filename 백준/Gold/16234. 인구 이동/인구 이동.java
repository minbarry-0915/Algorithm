import java.util.*;
import java.io.*;

public class Main {
    static int n,l,r;
    static int[][] map;
    static boolean[][] visited;
    static int[] dx = {0,0,-1,1};
    static int[] dy = {-1,1,0,0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        map = new int[n][n];
        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j ++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int days = 0;
        while (true){
            visited = new boolean[n][n];
            boolean moved = false;

            for (int i = 0; i < n; i ++){
                for (int j = 0; j < n; j ++){
                    if(!visited[i][j]){
                        if (bfs(i,j)) moved = true;

                    }
                }
            }

            if (!moved) break;
            days++;
        }
        System.out.println(days);
    }

    static boolean bfs(int x, int y){
        Queue<int[]> q = new LinkedList<>();
        List<int[]> union = new ArrayList<>();
        q.add(new int[]{x,y});
        union.add(new int[]{x,y});
        visited[x][y] = true;
        int sum = map[x][y];

        while (!q.isEmpty()){
            int[] curr = q.poll();
            int cx = curr[0], cy = curr[1];

            for (int d = 0; d < 4; d ++) {
                int nx = cx + dx[d];
                int ny = cy + dy[d];

                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]){
                    int diff = Math.abs(map[cx][cy] - map[nx][ny]);
                    if(diff >= l && diff <= r){
                        visited[nx][ny] = true;
                        q.add(new int[]{nx,ny});
                        union.add(new int[]{nx,ny});
                        sum += map[nx][ny];
                    }
                }
            }
        }

        if (union.size() == 1) return false; // 연합이 없음
        int newPopulation = sum / union.size(); // 연합의 인구수 / 연합을 이루고 있는 칸의 갯수
        // 인구수 조정
        for (int[] cell: union){
            map[cell[0]][cell[1]] = newPopulation;
        }
        return true;
    }

}