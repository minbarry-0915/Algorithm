function solution(s) {
    const stack = [];

    for (const char of s) {
        if (char === '(') {
            stack.push(char);
        } else if (char === ')') {
            if (stack.length === 0) return false;  // 닫는 괄호인데 열림이 없음
            stack.pop();  // 올바른 짝
        }
    }

    return stack.length === 0;  // 다 짝지어졌는지 확인
}