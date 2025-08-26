const dx = [1,0,0,-1]
const dy = [0,-1,1,0]
const dir = ['d','l','r','u']

function getManhattanDist(x1,y1,x2,y2){
    return Math.abs(x1 - x2) + Math.abs(y1 - y2)    
}

function solution(n, m, x, y, r, c, k) {
    let answer = []
    let result = 'impossible'
    let found = false
    
    
    function dfs(cx,cy,depth){
        if (found) return

        const dist = getManhattanDist(cx, cy, r, c);
        // 남은 횟수가 남은거리에 비해 부족할경우
        if (((k - depth) - dist) < 0){
            return
        }
        // 남는 횟수를 써야 하는데, 헛바퀴 돌고 와야 함 2배수 필요
        if (((k - depth) - dist) % 2 === 1){
            return
        }
        
        if (depth === k){
            if (cx === r && cy === c){
                result = answer.join('')
                found = true
            }
            return
        }
        
        
        for (let d = 0; d < 4; d ++){
            let nx = cx + dx[d]
            let ny = cy + dy[d]
            if (1 <= nx && nx <= n && 1 <= ny && ny <= m){
                answer.push(dir[d])
                dfs(nx,ny,depth + 1)
                answer.pop()
            }
        } 
    }
        
    dfs(x,y,0)
    return result

}