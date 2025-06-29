function solution(clothes) {
    const closet = {}
    
    for (const [item, type] of clothes){
        if(!closet[type]) closet[type] = 0;
        closet[type] ++;
    }
    
    let answer = 1;
    for (const type in closet){
        answer *= (closet[type] + 1);
    }
    
    return answer -1;
}