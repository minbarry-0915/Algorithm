const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

const s = Number(input[0]);

const visited = Array.from({ length: 1001 }, () => Array(1001).fill(-1));
queue = [];
queue.push([1, 0]);
visited[1][0] = 0;

while (queue.length > 0) {
	const [screen, clipboard] = queue.shift();

	if (screen === s) {
		console.log(visited[screen][clipboard]);
		break;
	}

	if (visited[screen][screen] === -1) {
		visited[screen][screen] = visited[screen][clipboard] + 1;
		queue.push([screen, screen]);
	}

	if (
		clipboard > 0 &&
		screen + clipboard < 1001 &&
		visited[screen + clipboard][clipboard] === -1
	) {
		visited[screen + clipboard][clipboard] = visited[screen][clipboard] + 1;
		queue.push([screen + clipboard, clipboard]);
	}

	if (screen > 0 && visited[screen - 1][clipboard] === -1) {
		visited[screen - 1][clipboard] = visited[screen][clipboard] + 1;
		queue.push([screen - 1, clipboard]);
	}
}
