const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

const n = Number(input[0]);

let start = 1;
let end = 1;
let sum = 1;
let count = 0;

while (start <= n) {
	if (sum < n) {
		end += 1;
		sum += end;
	} else if (sum > n) {
		sum -= start;
		start += 1;
	} else {
		count += 1;
		sum -= start;
		start += 1;
	}
}

console.log(count);
