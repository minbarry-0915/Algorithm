function solution(coin, cards) {
    const n = cards.length
    const required = n + 1
    
    // 초기 카드: 앞에서 n/3장
    let original = cards.slice(0, n / 3);
    // 추가 카드: 뽑을 때마다 추가
    let additional = [];
    
    let idx = Math.floor(n / 3)
    let answer = 0;
   
    // 접근 
    // 기존 가지고 있는 카드로 해결이 가능하면 동전 안쓰기
    // 카드 두개 뽑아서 하나만 구매해서 해결 가능하면 동전 1개 쓰기
    // 위의 방법으로 해결이 안되면 두개 다 사기
    // 카드가 없거나, 두 장을 낼수 없으면 종료
    
    while (true){
        if (idx >= n) break
        
        // 카드 두개 뽑기
        additional.push(cards[idx])
        additional.push(cards[idx + 1])
        idx += 2
        
        let flag = false
        
        // 기존 카드에서 해결이 가능한가?
        for (let i = 0; i < original.length; i++){
            const x = original[i]
            const target = required - x
            const j = original.indexOf(target)
            
            // 있고, 자기 자신 아니고
            if (j !== -1 && j !== i){
                // 두 카드를 낸다
                original = original.filter(x => x !== original[i] && x !== original[j])
                flag = true
                break
            }
        }
        
        // 1번 실패 : 코인 하나 내고 카드 하나 사면 해결이 가능한가?
        if (!flag && coin > 0){
            for (let i = 0; i < original.length; i++){
                const x = original[i]
                const target = required - x
                const j = additional.indexOf(target)
                
                // 있을 때
                if(j !== -1){
                    original = original.filter(x => x !== original[i])
                    additional = additional.filter(x => x !== additional[j])
                    coin--;
                    flag = true
                    break
                }
            }
        }
        
        // 2번 실패 : 코인 두개 내고 카드 두개 사서 해결이 가능한가?
        if (!flag && coin > 1){
            for (let i = 0; i < additional.length; i++){
                const x = additional[i]
                const target = required - x
                const j = additional.indexOf(target)
                
                if (j !== -1){
                    additional = additional.filter(x => x!== additional[i] && x !== additional[j])
                    coin -= 2
                    flag = true
                    break
                }
            }
        }
        
        // 3번도 실패
        if (!flag) break;
        answer ++
    }
    
    return answer + 1; // 실패한 마지막 라운드도 포함
}