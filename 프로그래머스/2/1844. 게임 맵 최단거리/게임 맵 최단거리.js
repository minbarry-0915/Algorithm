function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

   function bfs(sx, sy) {
    let visited = Array.from({ length: n }, () => Array(m).fill(-1));
    let queue = [];
    queue.push([sx, sy]);
    visited[sx][sy] = 1; // 시작 지점 거리 1

    while (queue.length > 0) {
        const [x, y] = queue.shift();

        for (let dir = 0; dir < 4; dir++) {
            const nx = x + dx[dir];
            const ny = y + dy[dir];

            if (
                nx >= 0 && nx < n &&
                ny >= 0 && ny < m &&
                maps[nx][ny] === 1 &&
                visited[nx][ny] === -1 // 방문 안 한 곳
            ) {
                visited[nx][ny] = visited[x][y] + 1;
                queue.push([nx, ny]);
            }
        }
    }

    return visited[n - 1][m - 1];
}


    return bfs(0, 0);
}