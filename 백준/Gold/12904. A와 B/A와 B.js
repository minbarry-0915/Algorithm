const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

let s = input[0].trim();
let t = input[1].trim();

while (t.length > s.length) {
	if (t[t.length - 1] === 'A') {
		t = t.slice(0, -1); // 마지막 문자 제거
	} else if (t[t.length - 1] === 'B') {
		t = t.slice(0, -1); // 마지막 문자 제거
		t = t.split('').reverse().join(''); // 뒤집기
	}
}

console.log(t === s ? 1 : 0);
