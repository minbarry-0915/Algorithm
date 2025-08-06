const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

const n = Number(input[0]);
const info = input[1].trim().split(' ').map(Number);

const result = Array(n).fill(0);

for (let i = 0; i < n; i++) {
	let taller = info[i];
	for (let j = 0; j < n; j++) {
		if (result[j] === 0) {
			if (taller === 0) {
				result[j] = i + 1;
				break;
			}
			taller--;
		}
	}
}

console.log(result.join(' '));
