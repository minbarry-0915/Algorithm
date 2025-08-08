const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

const n = Number(input[0]);
const t = [0];
const p = [0];

for (let i = 1; i <= n; i++) {
	const [a, b] = input[i].trim().split(" ").map(Number);
	t.push(a);
	p.push(b);
}

const dp = Array(n + 1).fill(0);

for (let i = 1; i < n + 1; i++) {
	if (i + t[i] - 1 <= n) {
		dp[i + t[i] - 1] = Math.max(dp[i + t[i] - 1], dp[i - 1] + p[i]);
	}
	dp[i] = Math.max(dp[i], dp[i - 1]);
}
console.log(dp[n]);
