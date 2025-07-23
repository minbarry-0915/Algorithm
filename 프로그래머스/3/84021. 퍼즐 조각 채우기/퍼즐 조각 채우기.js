function extractPieces(board, num){
    const n = board.length;
    let pieces = [];

    let visited = Array.from({length: n}, () => Array(n).fill(false));

    for (let i = 0; i < n; i++){
        for (let j = 0; j < n; j++){
            if (!visited[i][j] && board[i][j] === num){
                const piece = bfs(i, j, visited, board, num);
                pieces.push(piece);
            }
        }
    }

    return pieces;
}

const dx = [-1,1,0,0];
const dy = [0,0,-1,1];

function bfs(sx, sy, visited, board, num){
    const n = board.length;
    let queue = [[sx, sy]];
    visited[sx][sy] = true;

    let piece = [[sx, sy]];

    while (queue.length > 0){
        const [x, y] = queue.shift();

        for (let dir = 0; dir < 4; dir++){
            const nx = x + dx[dir];
            const ny = y + dy[dir];

            if (nx >= 0 && nx < n && ny >= 0 && ny < n){
                if (!visited[nx][ny] && board[nx][ny] === num){
                    visited[nx][ny] = true;
                    queue.push([nx, ny]);
                    piece.push([nx, ny]);
                }
            }
        }
    }

    // 정규화
    const minX = Math.min(...piece.map(([x]) => x));
    const minY = Math.min(...piece.map(([_, y]) => y));
    piece = piece.map(([x, y]) => [x - minX, y - minY]);
    piece.sort((a,b) => a[0] - b[0] || a[1] - b[1]);

    return piece;
}

function rotateBlock(block, times){
    let rotated = block.map(([x, y]) => [x, y]);

    for (let t = 0; t < times; t++){
        rotated = rotated.map(([x, y]) => [y, -x]);
        const minX = Math.min(...rotated.map(([x]) => x));
        const minY = Math.min(...rotated.map(([_, y]) => y));
        rotated = rotated.map(([x, y]) => [x - minX, y - minY]);
        rotated.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    }

    return rotated;
}

function isSame(hole, piece){
    if (hole.length !== piece.length) return false;

    for (let i = 0; i < hole.length; i++){
        const [hx, hy] = hole[i];
        const [px, py] = piece[i];
        if (hx !== px || hy !== py) return false;
    }

    return true;
}

function solution(game_board, table) {
    const puzzlePieces = extractPieces(table, 1);
    const emptySpaces = extractPieces(game_board, 0);

    const used = Array(puzzlePieces.length).fill(false);
    let answer = 0;

    for (const hole of emptySpaces){
        for (let i = 0; i < puzzlePieces.length; i++){
            if (used[i]) continue;

            for (let r = 0; r < 4; r++){
                const rotated = rotateBlock(puzzlePieces[i], r);
                if (isSame(hole, rotated)){
                    answer += hole.length;
                    used[i] = true;
                    break;
                }
            }

            if (used[i]) break;
        }
    }

    return answer;
}
