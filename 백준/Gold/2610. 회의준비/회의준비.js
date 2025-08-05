const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

const n = Number(input[0]);
const m = Number(input[1]);
const dist = Array.from({ length: n + 1 }, () => Array(n + 1).fill(Infinity));

// 자기 자신까지 거리 0
for (let i = 1; i <= n; i++) {
	dist[i][i] = 0;
}

for (let i = 2; i < 2 + m; i++) {
	const [a, b] = input[i].trim().split(" ").map(Number);
	dist[a][b] = 1;
	dist[b][a] = 1;
}

// 플로이드-워셜
for (let k = 1; k <= n; k++) {
	for (let i = 1; i <= n; i++) {
		for (let j = 1; j <= n; j++) {
			if (dist[i][k] + dist[k][j] < dist[i][j]) {
				dist[i][j] = dist[i][k] + dist[k][j];
			}
		}
	}
}

// 그룹 나누기
const visited = Array(n + 1).fill(false);
const groups = [];

for (let i = 1; i <= n; i++) {
	if (!visited[i]) {
		const group = [];
		const queue = [i];
		visited[i] = true;

		while (queue.length > 0) {
			const cur = queue.shift();
			group.push(cur);

			for (let j = 1; j <= n; j++) {
				if (!visited[j] && dist[cur][j] !== Infinity) {
					visited[j] = true;
					queue.push(j);
				}
			}
		}

		groups.push(group);
	}
}

// 대표자 선정
const representatives = [];

for (const group of groups) {
	let minScore = Infinity;
	let representative = -1;

	for (const person of group) {
		let score = 0;
		for (const other of group) {
			score = Math.max(score, dist[person][other]);
		}

		if (score < minScore) {
			minScore = score;
			representative = person;
		}
	}

	representatives.push(representative);
}

representatives.sort((a, b) => a - b);

// 출력
console.log(representatives.length);
for (const rep of representatives) {
	console.log(rep);
}
