function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    
    let deliverIdx = n - 1;
    let pickupIdx = n - 1;
    
    while (deliverIdx >= 0 || pickupIdx >= 0){
        let deliverLoad = 0
        let pickupLoad = 0
        
        while (deliverIdx >= 0 && deliveries[deliverIdx] === 0){
            deliverIdx--;
        }
        
        while (pickupIdx >= 0 && pickups[pickupIdx] === 0){
            pickupIdx--
        }
        
        if (deliverIdx < 0 && pickupIdx < 0) break
        
        const tripDistance = Math.max(deliverIdx, pickupIdx) + 1
        answer += tripDistance * 2
        
        let capRemain = cap
        while (deliverIdx >= 0 && capRemain > 0){
            if (deliveries[deliverIdx] > 0){
                if (deliveries[deliverIdx] <= capRemain){
                    capRemain -= deliveries[deliverIdx]
                    deliveries[deliverIdx] = 0
                    deliverIdx--
                }else{
                    deliveries[deliverIdx] -= capRemain
                    capRemain = 0
                }
            }else{
                deliverIdx--
            }
        }
        
        capRemain = cap
        while (pickupIdx >= 0 && capRemain > 0){
            if (pickups[pickupIdx] > 0){
                if (pickups[pickupIdx] <= capRemain){
                    capRemain -= pickups[pickupIdx]
                    pickups[pickupIdx] = 0
                    pickupIdx--
                }else{
                    pickups[pickupIdx] -= capRemain
                    capRemain = 0
                }
            }else{
                pickupIdx--
            }
        }
    }
    
    return answer
}