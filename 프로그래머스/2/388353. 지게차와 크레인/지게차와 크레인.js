    
const dx = [-1,1,0,0]
const dy = [0,0,-1,1]

function solution(storage, requests) {
    const n = storage.length
    const m = storage[0].length
    
    // Padding
    const newStorage = [Array(m + 2).fill('0')]
    for (const s of storage){
        const row = ['0']
        for (let i = 0; i < m; i ++){
            row.push(s[i])
        }
        row.push('0')
        newStorage.push(row)
    }
    newStorage.push(Array(m + 2).fill('0'))
    
    // Request Handling
    requests.forEach(r => {
        if (r.length === 1){
            fork(r)
        }
        else {
            crain(r)
        }
    })
    
    function update () {
        const queue = []
        const visited = Array.from({length: n + 2},() => Array(m + 2).fill(false))
        queue.push([0,0])
        visited[0][0] = true
        
        while (queue.length > 0){
            const [x,y] = queue.shift()
            
            for (let d = 0; d < 4; d ++){
                const nx = x + dx[d]
                const ny = y + dy[d]
                
                if (0 <= nx && nx < n + 2 && 0 <= ny && ny < m + 2 && !visited[nx][ny]){
                    if (newStorage[nx][ny] === '0'){
                        visited[nx][ny] = true
                        queue.push([nx,ny])
                    }
                    else if (newStorage[nx][ny] == '1'){
                        newStorage[nx][ny] = '0'
                        visited[nx][ny] = true
                        queue.push([nx,ny])
                    }
                }
            }
        }
        return
    }
    
    function fork (request) {
        const buffer = []
        
        for (let i = 0; i < n + 2; i ++){
            for (let j = 0; j < m + 2; j ++){
                if (newStorage[i][j] === request){
                    for (let d = 0; d < 4; d ++){
                        const nx = i + dx[d]
                        const ny = j + dy[d]
                        // 주위에 빈칸이 있는경우
                        if (0 <= nx && nx < n + 2 && 0 <= ny && ny < m + 2 && newStorage[nx][ny] === '0'){
                            buffer.push([i,j])
                            break
                        }
                    }
                }
            }
        }
        
        for (const [x,y] of buffer){
            newStorage[x][y] = '0'
        }
        update()
        return
    }
    
    function crain (request) {
        const target = request[0]
        const buffer = []
        
        for (let i = 0; i < n + 2; i ++){
            for (let j = 0; j < m + 2; j ++){
                if (newStorage[i][j] === target){
                    buffer.push([i,j])
                }
            }
        }
        
        for (const [x,y] of buffer){
            newStorage[x][y] = '1'
        }
        
        update()
        return
    }
    
    for (const s of newStorage) console.log(...s)
    
    let answer = 0
    for (let i = 1; i < n + 1; i ++){
        for (let j = 1; j < m + 1; j ++){
            if (newStorage[i][j] !== '0' && newStorage[i][j] !== '1') answer++
        }
    }
    return answer
}