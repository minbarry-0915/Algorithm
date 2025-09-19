import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        //System.setIn(new FileInputStream("input.txt"));
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

       int n = Integer.parseInt(br.readLine());
       int m = Integer.parseInt(br.readLine());

       int[] dp = new int[n + 1];
       dp[0] = 1;
       dp[1] = 1;
       for (int i = 2; i <= n; i++){
           dp[i] = dp[i - 1] + dp[i - 2];
       }
       int answer = 1;
       int pre = 0;
       for (int i = 0; i < m; i ++){
           int k = Integer.parseInt(br.readLine());
           answer *= dp[k - pre - 1];
           pre = k;
       }
       answer *= dp[n - pre];
       System.out.println(answer);
    }


}