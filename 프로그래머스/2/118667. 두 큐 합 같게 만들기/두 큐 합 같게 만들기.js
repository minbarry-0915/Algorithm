function solution(queue1, queue2) {
    let currentSum = queue1.reduce((acc, val) => acc + val, 0);
    const totalSum = currentSum + queue2.reduce((acc, val) => acc + val, 0);

    if (totalSum % 2 !== 0) {
        return -1;
    }

    const target = totalSum / 2;
    const combined = [...queue1, ...queue2];
    
    let start = 0;
    let end = queue1.length;
    let moves = 0;
    
    // 무한 루프 방지를 위한 최대 연산 횟수
    const limit = 300000;

    while (moves < limit) {
        if (currentSum === target) {
            return moves;
        }

        if (currentSum > target) {
            currentSum -= combined[start];
            start++;
        } else {
            // end가 배열의 끝에 도달하면 더 이상 옮길 원소가 없으므로 종료
            if (end >= combined.length) {
                break;
            }
            currentSum += combined[end];
            end++;
        }
        moves++;
    }

    return -1;
}