function solution(n, computers) {
    let graph = {};

    // 1. 그래프 만들기
    for (let i = 0; i < n; i++) {
        graph[i] = [];
        for (let j = 0; j < n; j++) {
            if (i !== j && computers[i][j] === 1) {
                graph[i].push(j);
            }
        }
    }

    // 2. 방문 배열 & 네트워크 수 세기
    let visited = Array(n).fill(false);
    let count = 0;

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            bfs(i, visited, graph);
            count += 1;
        }
    }

    return count;
}

function bfs(start, visited, graph) {
    let queue = [];
    queue.push(start);
    visited[start] = true;

    while (queue.length > 0) {
        let current = queue.shift();
        for (let next of graph[current]) {
            if (!visited[next]) {
                queue.push(next);
                visited[next] = true;
            }
        }
    }
}
