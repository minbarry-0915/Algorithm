const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

const n = Number(input[0]);
const numList = [];

for (let i = 1; i < n + 1; i++) {
	const num = Number(input[i]);
	numList.push(num);
}

const dp = Array(n).fill(1);

for (let i = 0; i < n; i++) {
	for (let j = 0; j < i; j++) {
		if (numList[j] < numList[i]) {
			dp[i] = Math.max(dp[i], dp[j] + 1);
		}
	}
}

console.log(n - Math.max(...dp));
