const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

const directions = [
	[0, -1, 0],
	[0, 1, 0], // x축 (상하)
	[0, 0, -1],
	[0, 0, 1], // y축 (좌우)
	[-1, 0, 0],
	[1, 0, 0], // z축 (층 위아래)
];

let lineIndex = 0;

function isInBoundary(z, x, y, l, r, c) {
	return z >= 0 && z < l && x >= 0 && x < r && y >= 0 && y < c;
}

function bfs(building, start, end, l, r, c) {
	const visited = Array.from({ length: l }, () =>
		Array.from({ length: r }, () => Array(c).fill(false))
	);
	const [sz, sx, sy] = start;
	const [ez, ex, ey] = end;

	const queue = [];
	queue.push([...start, 0]);
	visited[sz][sx][sy] = true;

	while (queue.length > 0) {
		const [z, x, y, time] = queue.shift();

		if (z === ez && x === ex && y === ey) {
			return `Escaped in ${time} minute(s).`;
		}

		for (const [dz, dx, dy] of directions) {
			const [nz, nx, ny] = [z + dz, x + dx, y + dy];

			if (
				isInBoundary(nz, nx, ny, l, r, c) &&
				!visited[nz][nx][ny] &&
				building[nz][nx][ny] !== '#'
			) {
				visited[nz][nx][ny] = true;
				queue.push([nz, nx, ny, time + 1]);
			}
		}
	}

	return 'Trapped!';
}

function parseBuilding(l, r, c) {
	const building = [];
	let start = null;
	let end = null;

	for (let z = 0; z < l; z++) {
		const floor = [];
		for (let x = 0; x < r; x++) {
			const row = input[lineIndex++].split('');
			row.forEach((cell, y) => {
				if (cell === 'S') start = [z, x, y];
				if (cell === 'E') end = [z, x, y];
			});
			floor.push(row);
		}
		building.push(floor);
		lineIndex++;
	}

	return { building, start, end };
}
while (true) {
	const [l, r, c] = input[lineIndex++].split(' ').map(Number);

	if (l === 0 && r === 0 && c === 0) break;

	const { building, start, end } = parseBuilding(l, r, c);
	const result = bfs(building, start, end, l, r, c);
	console.log(result);
}
