function solution(s) {
    const lst = s.split(' ').map(Number)
    return `${Math.min(...lst)} ${Math.max(...lst)}`
}