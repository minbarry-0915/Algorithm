function solution(rectangle, characterX, characterY, itemX, itemY) {
  const MAX = 102;
  const grid = Array.from({ length: MAX }, () => Array(MAX).fill(-1));
  const visited = Array.from({ length: MAX }, () => Array(MAX).fill(0));

  // 1. 직사각형 테두리 그리기
  for (const rect of rectangle) {
    const [lx, ly, rx, ry] = rect.map(v => v * 2);

    for (let i = lx; i <= rx; i++) {
      for (let j = ly; j <= ry; j++) {
        // 내부 채우기
        if (lx < i && i < rx && ly < j && j < ry) {
          grid[i][j] = 0; // 내부
        } else if (grid[i][j] !== 0) {
          grid[i][j] = 1; // 테두리
        }
      }
    }
  }

  // 2. BFS
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  const queue = [];
  const startX = characterX * 2;
  const startY = characterY * 2;
  const endX = itemX * 2;
  const endY = itemY * 2;

  queue.push([startX, startY]);

  while (queue.length > 0) {
    const [x, y] = queue.shift();

    if (x === endX && y === endY) {
      return visited[x][y] / 2;
    }

    for (let d = 0; d < 4; d++) {
      const nx = x + dx[d];
      const ny = y + dy[d];

      if (nx > 0 && ny > 0 && nx < MAX && ny < MAX) {
        if (visited[nx][ny] === 0 && grid[nx][ny] === 1) {
          visited[nx][ny] = visited[x][y] + 1;
          queue.push([nx, ny]);
        }
      }
    }
  }

  return 0;
}
