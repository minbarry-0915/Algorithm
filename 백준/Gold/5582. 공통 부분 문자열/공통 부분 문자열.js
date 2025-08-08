const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

const s1 = input[0].trim().split("");
const s2 = input[1].trim().split("");
const n1 = s1.length;
const n2 = s2.length;

const dp = Array.from({ length: n2 + 1 }, () => Array(n1 + 1).fill(0));
let answer = 0;

// 부분 문자열은 연속 해야됨 -> 연속하지 않으면 초기화!
for (let i = 1; i < n2 + 1; i++) {
	for (let j = 1; j < n1 + 1; j++) {
		if (s2[i - 1] === s1[j - 1]) {
			dp[i][j] = dp[i - 1][j - 1] + 1;
			if (dp[i][j] > answer) answer = dp[i][j];
		} else {
			dp[i][j] = 0;
		}
	}
}

console.log(answer);
