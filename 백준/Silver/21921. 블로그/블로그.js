const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

const [n, x] = input[0].split(' ').map(Number);
const visitors = input[1].split(' ').map(Number);

let sum = visitors.slice(0, x).reduce((a, b) => a + b, 0);
let max = sum;
let count = sum === 0 ? 0 : 1;

for (let i = x; i < n; i++) {
	sum += visitors[i] - visitors[i - x];

	if (sum > max) {
		max = sum;
		count = 1;
	} else if (sum === max) {
		count++;
	}
}
console.log(max === 0 ? 'SAD' : `${max}\n${count}`);
