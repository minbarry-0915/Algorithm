const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split(' ');

const g = Number(input[0]);

let x = 2;
let y = 1;
const result = [];

while (x <= 100000) {
	const diff = x * x - y * y;

	if (diff === g) {
		result.push(x);
		x++;
	} else if (diff < g) {
		x++;
	} else {
		y++;
	}
}

console.log(result.length ? result.join('\n') : -1);
