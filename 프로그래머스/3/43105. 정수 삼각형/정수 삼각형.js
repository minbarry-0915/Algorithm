function solution(triangle) {
    const n = triangle.length;
    const dp = Array.from({length: triangle.length}, 
                          (_, i) => Array(triangle[i].length).fill(0))
    
    dp[0][0] = triangle[0][0]
    
    for (let i = 1; i < n; i ++){
        for (let j = 0; j <triangle[i].length; j++){
            if (j === 0){
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            }else if(j === triangle[i].length - 1){
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            }else{
                dp[i][j] = Math.max(dp[i - 1][j - 1],dp[i - 1][j]) + triangle[i][j]
            }
        }
    }
    
    let answer = 0;
    for (let val of dp[n - 1]) {
        answer = Math.max(answer, val);
    }
    return answer;
}