const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

const n = Number(input[0]);
const nums = input[1].trim().split(" ").map(Number);

const dp = Array.from({ length: n - 1 }, () => Array(21).fill(BigInt(0)));
dp[0][nums[0]] = BigInt(1);

for (let i = 1; i < n - 1; i++) {
	for (let val = 0; val < 21; val++) {
		if (dp[i - 1][val] > 0) {
			const plus = val + nums[i];
			const minus = val - nums[i];

			if (0 <= plus && plus <= 20) dp[i][plus] += dp[i - 1][val];
			if (0 <= minus && minus <= 20) dp[i][minus] += dp[i - 1][val];
		}
	}
}

console.log(String(dp[n - 2][nums[n - 1]]));
