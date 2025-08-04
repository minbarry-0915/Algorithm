
const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

const code = input[0].trim().split("").map(Number);
const n = code.length;
const MOD = 1000000;

if (n === 0 || code[0] === 0) {
	console.log(0);
	process.exit(0);
}

const dp = Array(n + 1).fill(0);
dp[0] = 1;
dp[1] = 1;

for (let k = 1; k < n; k++) {
	const i = k + 1;
	if (code[k] > 0) {
		dp[i] = (dp[i] + dp[i - 1]) % MOD;
	}
	const twoDigit = code[k - 1] * 10 + code[k];
	if (twoDigit >= 10 && twoDigit <= 26) {
		dp[i] = (dp[i] + dp[i - 2]) % MOD;
	}
}

console.log(dp[n] % MOD);
