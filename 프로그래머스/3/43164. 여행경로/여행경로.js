function solution(tickets) {
    const routes = [];
    const visited = Array(tickets.length).fill(false);

    tickets.sort(); // 사전순 정렬

    function dfs(path, count) {
        if (count === tickets.length) {
            routes.push([...path]);
            return;
        }

        for (let i = 0; i < tickets.length; i++) {
            const [from, to] = tickets[i];
            if (!visited[i] && path[path.length - 1] === from) {
                visited[i] = true;
                path.push(to);
                dfs(path, count + 1);
                path.pop();
                visited[i] = false;
            }
        }
    }

    dfs(['ICN'], 0);
    return routes[0]; // 정렬했기 때문에 첫 번째 경로가 사전순으로 가장 빠름
}
