function solution(dice) {
    const n = dice.length
    const half = n / 2
    let bestpick = []
    let maxWin = -1; 
    
    const getSums = (selected) => {
        let sums = [0]
        for (const dice of selected){
            const next = []
            for (const s of sums){
                for (const face of dice){
                    next.push(s + face)
                }
            }
            sums = next
        }
        
        return sums 
    }
    
    const combinations = (arr, k, start = 0, chosen = []) => {
        if (chosen.length === k){
            const remain = arr.filter(x => !chosen.includes(x))
            const sumA = getSums(chosen.map(i => dice[i]))
            const sumB = getSums(remain.map(i => dice[i]))
            sumA.sort((a,b) => a - b)
            sumB.sort((a,b) => a - b) 
            
            let win = 0
            // sumB는 정렬되어있음
            for (const a of sumA) {
              // sumB에서 a보다 작은 값 개수 찾기 (이진탐색)
              let left = 0, right = sumB.length;
              while (left < right) {
                let mid = Math.floor((left + right) / 2);
                if (sumB[mid] < a) left = mid + 1;
                else right = mid;
              }
              win += left; // left가 a보다 작은 값 개수
            }
            
            const total = sumA.length * sumB.length;
            const rate = win / total
            
            if (maxWin < rate){
                maxWin = rate
                bestPick = [...chosen.map(x => x + 1)]
            }
            return;
        }
        
        for (let i = start; i < n; i ++){
            chosen.push(arr[i])
            combinations(arr, k, i + 1, chosen)
            chosen.pop()
        }
    }

    combinations([...Array(n).keys()], half)
    return bestPick
}