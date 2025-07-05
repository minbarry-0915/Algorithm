function solution(arr) {
    const result = [];

    for (let i = 0; i < arr.length; i++) {
        // 이전 값과 다를 때만 추가
        if (result[result.length - 1] !== arr[i]) {
            result.push(arr[i]);
        }
    }

    return result;
}
