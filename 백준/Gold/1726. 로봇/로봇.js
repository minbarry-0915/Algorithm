const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

// 동 남 서 북
const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

const dirToIdx = {
	1: 0,
	2: 2,
	3: 1,
	4: 3,
};

const [n, m] = input[0].trim().split(' ').map(Number);
const grid = Array.from({ length: n }, (_, idx) =>
	input[idx + 1].trim().split(' ').map(Number)
);
let [sx, sy, sd] = input[n + 1].trim().split(' ').map(Number);
[sx, sy, sd] = [sx - 1, sy - 1, dirToIdx[sd]];
let [ex, ey, ed] = input[n + 2].trim().split(' ').map(Number);
[ex, ey, ed] = [ex - 1, ey - 1, dirToIdx[ed]];

const visited = Array.from({ length: n }, () =>
	Array.from({ length: m }, () => Array(4).fill(-1))
);

queue = [];
queue.push([sx, sy, sd, 0]);
visited[sx][sy][sd] = 0;

while (queue.length > 0) {
	const [x, y, cd, cnt] = queue.shift();

	if (x === ex && y === ey && cd === ed) {
		console.log(visited[ex][ey][ed]);
		break;
	}

	for (let k = 1; k < 4; k++) {
		const nx = x + k * dx[cd];
		const ny = y + k * dy[cd];

		if (!(nx >= 0 && nx < n && ny >= 0 && ny < m)) break;
		if (grid[nx][ny] === 1) break;
		if (visited[nx][ny][cd] === -1) {
			visited[nx][ny][cd] = cnt + 1;
			queue.push([nx, ny, cd, cnt + 1]);
		}
	}

	// 오른쪽
	let nd = (cd + 1) % 4;
	if (visited[x][y][nd] === -1) {
		visited[x][y][nd] = cnt + 1;
		queue.push([x, y, nd, cnt + 1]);
	}

	nd = (cd + 3) % 4;
	if (visited[x][y][nd] === -1) {
		visited[x][y][nd] = cnt + 1;
		queue.push([x, y, nd, cnt + 1]);
	}
}
