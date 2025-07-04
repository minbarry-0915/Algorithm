function solution(participant, completion) {
    const counter = new Map()
    
    for (const name of participant){
        counter.set(name, (counter.get(name) || 0) + 1)
    }
    
    for (const name of completion){
        counter.set(name, (counter.get(name) - 1))
    }
    
    for (const [name, count] of counter){
        if (count > 0) return name;
        
    }
}