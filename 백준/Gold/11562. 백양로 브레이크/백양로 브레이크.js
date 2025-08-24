const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf-8').trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const graph = Array.from({ length: n + 1 }, () => Array(n + 1).fill(Infinity));

for (let i = 1; i <= m; i++) {
	const [u, v, b] = input[i].split(' ').map(Number);

	if (b === 1) {
		graph[u][v] = 0;
		graph[v][u] = 0;
	} else {
		graph[u][v] = 0;
		graph[v][u] = 1;
	}
}

for (let i = 1; i < n + 1; i++) {
	graph[i][i] = 0;
}

const k = parseInt(input[m + 1].trim());

for (let q = 1; q < n + 1; q++) {
	for (let i = 1; i < n + 1; i++) {
		for (let j = 1; j < n + 1; j++) {
			if (graph[i][j] > graph[i][q] + graph[q][j]) {
				graph[i][j] = graph[i][q] + graph[q][j];
			}
		}
	}
}

for (let i = m + 2; i < m + 2 + k; i++) {
	const [s, e] = input[i].split(' ').map(Number);
	console.log(graph[s][e] === Infinity ? -1 : graph[s][e]);
}
