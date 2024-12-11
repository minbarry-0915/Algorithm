// 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

const fs = require('fs');
const input = fs.readFileSync(process.platform === 'linux' ? "/dev/stdin" : "./input.txt").toString().trim();  
const score = parseInt(input);

if (score >= 90 && score <= 100){
    console.log('A')
}else if (score >= 80 && score <= 89){
    console.log('B')
}else if (score >= 70 && score <= 79){
    console.log('C')
}else if (score >= 60 && score <= 69){
    console.log('D')
}else{
    console.log('F')
}