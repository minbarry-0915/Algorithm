const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const edges = input.slice(1, m + 1).map((line) => line.split(' ').map(Number));
const [start, end] = input[m + 1].split(' ').map(Number);

const graph = Array.from({ length: n + 1 }, () => []);

for (const [a, b, w] of edges) {
	graph[a].push([b, w]);
	graph[b].push([a, w]);
}

function bfs(limit) {
	const visited = Array(n + 1).fill(false);
	const queue = [start];
	visited[start] = true;

	while (queue.length > 0) {
		const cur = queue.shift();
		if (cur === end) return true;

		for (const [next, weight] of graph[cur]) {
			if (!visited[next] && weight >= limit) {
				visited[next] = true;
				queue.push(next);
			}
		}
	}

	return false;
}

let left = 1;
let right = 1e9; // 충분히 큰 값으로 설정
let answer = 0;

while (left <= right) {
	const mid = Math.floor((left + right) / 2);

	if (bfs(mid)) {
		answer = mid;
		left = mid + 1;
	} else {
		right = mid - 1;
	}
}

console.log(answer);
