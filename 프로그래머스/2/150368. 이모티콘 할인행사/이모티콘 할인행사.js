function solution(users, emoticons) {
    const n = emoticons.length;
    const discountRates = [10, 20, 30, 40];
    const cases = [];

    function dfs(depth, arr) {
        if (depth === n) {
          cases.push([...arr]);
          return;
        }

        for (const rate of discountRates) {
            arr.push(rate);
            dfs(depth + 1, arr);
            arr.pop();
        }
    }
    
    dfs(0, [])
    
    function simulation(rates){
        // 각 이모지의 할인율을 적용한 가격을 계산
        // 긱 사용자의 구매 기준 할인율에 따라서 사용자의 총 구매 비용 계산
        // 긱 사용자의 구매 기준 가격에 따라서 이상일 경우 이모티콘 플러스, 아닐경우 구매비용
        // 총 이모티콘 플러스 유저, 매출 리턴
        
        const discountedEmojis = rates.map((rate, idx) => ( 
            {rate: rate,
             price: emoticons[idx] * (100 - rate) / 100
            }
        ))
        
        let plusUsersNum = 0
        let incomes = 0
        users.forEach(user => {
            const [thresholdRate, thresholdPrice] = user
            let totalPrice = 0
            discountedEmojis.forEach(emoji => {
                if (emoji['rate'] >= thresholdRate){
                    totalPrice += emoji['price']
                }
            })
            if (totalPrice >= thresholdPrice) plusUsersNum ++
            else incomes += totalPrice
        })
        return [plusUsersNum,incomes]
    }
    
    let currentPlusUsersNum = 0
    let currentIncomes = 0
    
    for (const c of cases){
        const [plusUsersNum, incomes] = simulation(c)
        // 1순위 플러스 유저수를 늘려야된다.
        // 2순위 매출을 늘려야된다. 
        if (plusUsersNum > currentPlusUsersNum) {
            currentPlusUsersNum = plusUsersNum;
            currentIncomes = incomes;
        } else if (plusUsersNum === currentPlusUsersNum && incomes > currentIncomes) {
            currentIncomes = incomes;
        }
    }
    
    return [currentPlusUsersNum, currentIncomes]
}