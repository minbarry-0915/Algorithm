function solution(numbers, target) {
    let count = 0;

    function dfs(depth, total) {
        if (depth === numbers.length) {
            if (total === target) count += 1;
            return;
        }
        dfs(depth + 1, total + numbers[depth]);
        dfs(depth + 1, total - numbers[depth]);
    }

    dfs(0, 0);
    return count;
}
