const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

const [n, m] = input[0].trim().split(' ').map(Number);
const grid = [];
grid.push(Array(m + 1).fill('0'));
for (let i = 1; i < n + 1; i++) {
	grid.push(['0', ...input[i].trim().split('')]);
}

const dp = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0));

let maxLen = 0;
for (let i = 1; i < n + 1; i++) {
	for (let j = 1; j < m + 1; j++) {
		if (grid[i][j] === '1') {
			dp[i][j] = Math.min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1;
			maxLen = Math.max(maxLen, dp[i][j]);
		}
	}
}

console.log(Math.pow(maxLen, 2));
