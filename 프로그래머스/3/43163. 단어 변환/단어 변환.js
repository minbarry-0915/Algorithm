function solution(begin, target, words) {
    const n = words.length;
    let queue = [];
    let visited = Array(n).fill(false);

    // 큐에 단어와 변환 횟수 같이 저장
    queue.push([begin, 0]);

    while (queue.length > 0) {
        const [current, count] = queue.shift();

        if (current === target) return count;

        for (let i = 0; i < n; i++) {
            if (!visited[i] && isOneCharDiff(current, words[i])) {
                visited[i] = true;
                queue.push([words[i], count + 1]);
            }
        }
    }

    return 0; // target에 도달 못 하면 0 반환

    function isOneCharDiff(str1, str2) {
        if (str1.length !== str2.length) return false;

        let diffCount = 0;
        for (let i = 0; i < str1.length; i++) {
            if (str1[i] !== str2[i]) {
                diffCount++;
                if (diffCount > 1) return false;
            }
        }
        return diffCount === 1;
    }
}
