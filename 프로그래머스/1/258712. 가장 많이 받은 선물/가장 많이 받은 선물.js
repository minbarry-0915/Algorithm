function solution(friends, gifts) {
    const n = friends.length
    const nameToIdx = {
    }
    for (let i = 0; i < n; i++){
        nameToIdx[friends[i]] = i
    }
    const answer = Array(n).fill(0);
    
    const presentCounter = Array.from({length: n}, ()=> Array(n).fill(0))
    const presentIndices = Array.from({length: n}, ()=> Array(3).fill(0))
    
    // 선물 기록
    for (const gift of gifts){
        const [from, to] = gift.trim().split(' ')
        const fromIdx = nameToIdx[from]       
        const toIdx = nameToIdx[to]        
        presentCounter[fromIdx][toIdx] += 1
        presentIndices[fromIdx][0] += 1
        presentIndices[toIdx][1] += 1
    }
    
    // 선물지수 계산
    for (let i = 0; i < n; i ++){
        presentIndices[i][2] = presentIndices[i][0] - presentIndices[i][1]
    }
    
    // 결과 계산
    const additionalPresent = Array(n).fill(0)
    
    for (let i = 0; i < n; i++){
        for (let j = 0; j < n; j++){
            if (i === j) continue // 자기 자신은 패스
            
            if (presentCounter[i][j] > presentCounter[j][i]){
                additionalPresent[i] += 1
            } else if (presentCounter[i][j] === presentCounter[j][i]){
                // 같을 경우 선물 지수 비교
                if (presentIndices[i][2] > presentIndices[j][2]){
                    additionalPresent[i] += 1
                }
            }
        }
    }

    let maxCount = -1
    for (const count of additionalPresent){
        maxCount = Math.max(maxCount, count)
    }

    return maxCount
}