function solution(distance, rocks, n) {
    rocks.sort((a,b) => a - b)
    console.log(rocks)
    
    let left = 0
    let right = distance
    let answer = 0
    
    while (left <= right){
        const mid = Math.floor((left + right) / 2)
        let removeRocks = 0
        let prev = 0
        
        rocks.forEach(rock => {
            if (rock - prev < mid){
                removeRocks ++
            }else{
                prev = rock
            }
        })
        
        if (distance - prev < mid) removeRocks ++ 
        
        if (removeRocks > n){
            right = mid - 1
        }else{
            answer = mid
            left = mid + 1
        }
    }
    return answer
}