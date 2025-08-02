const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

const [n, k] = input[0].split(' ').map(Number);
const cost = input.slice(1).map((line) => line.split(' ').map(Number));

// 1. floyd warshall
for (let m = 0; m < n; m++) {
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < n; j++) {
			if (cost[i][m] + cost[m][j] < cost[i][j]) {
				cost[i][j] = cost[i][m] + cost[m][j];
			}
		}
	}
}

// 2. dfs + backtracking
let minCost = Infinity;
const visited = Array(n).fill(false);

function dfs(current, count, total) {
	if (count === n) {
		minCost = Math.min(minCost, total);
		return;
	}

	for (let next = 0; next < n; next++) {
		if (!visited[next]) {
			visited[next] = true;
			dfs(next, count + 1, total + cost[current][next]);
			visited[next] = false;
		}
	}
}

visited[k] = true;
dfs(k, 1, 0);
console.log(minCost);
