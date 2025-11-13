function solution(targets) {
    targets.sort((a,b) => {
        if (a[1] !== b[1]) return a[1] - b[1]
        return a[0] - b[0]
    })
    
    let end = 0
    let answer = 0 
    for (let t of targets){
        if (t[0] >= end){
            end = t[1]
            answer ++
        }
    }
    return answer
}