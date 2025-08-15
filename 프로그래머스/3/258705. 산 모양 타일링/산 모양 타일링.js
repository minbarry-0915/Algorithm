function solution(n, tops) {
    // dp[i][0] 은 오른쪽 방향 마름모만 고려
    // dp[i][1] 은 나머지 방향 마름모를 넣었을때
    const MOD = 10007
    const dp = Array.from({length: n}, () => Array(2).fill(0))
    dp[0][0] = 1
    if (tops[0] === 1){
        dp[0][1] = 3
    }else{
        dp[0][1] = 2
    }
     
    
    for (let i = 1; i < n; i++){
        if (tops[i] === 1){
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][1] = (dp[i - 1][0] * 2 + dp[i - 1][1] * 3) % MOD
        }else{
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] * 2) % MOD
        }
    }
        
    return (dp[n - 1][0] + dp[n - 1][1]) % MOD;
}

