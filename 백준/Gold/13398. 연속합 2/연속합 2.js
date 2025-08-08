const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

const n = Number(input[0]);
const arr = input[1].trim().split(" ").map(Number);

const dp = Array.from({ length: n }, () => Array(2).fill(0));
dp[0][0] = arr[0];
dp[0][1] = 0;

let answer = arr[0];

for (let i = 1; i < n; i++) {
	dp[i][0] = Math.max(dp[i - 1][0] + arr[i], arr[i]);
	dp[i][1] = Math.max(dp[i - 1][1] + arr[i], dp[i - 1][0]);
	answer = Math.max(answer, dp[i][0], dp[i][1]);
}

console.log(answer);
