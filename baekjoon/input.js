//입력값 여러 개
function inputMult() {
    const fs = require('fs');
    const input = fs.readFileSync('/dev/stdin').toString().trim().split(" ");
}


//입력값 여러 줄
function inputMultLine() {
    const fs = require('fs');
    const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
}

// 4. 입력값이 첫 번째 줄에는 입력 값의 길이(n), 두 번째 줄에 공백으로 구분된 입력값이 주어질 때
/* ex)
3
110 78 158
*/
const fs = require('fs');
const [n, input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const inputArr = input.trim().split(" ");

// 5. 입력값이 첫 번째 줄에는 입력 값의 길이(n), n개의 줄에 걸쳐서 한 줄에 하나의 입력값이 주어질 때
/* ex)
3
110
78
158
*/
const fs = require('fs');
const [n, input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');


