const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

const [n, r, c] = input[0].trim().split(' ').map(Number);

function sol(n, r, c) {
	if (n === 0) return 0;

	return (
		2 * (r % 2) + (c % 2) + 4 * sol(n - 1, Math.floor(r / 2), Math.floor(c / 2))
	);
}

console.log(sol(n, r, c));
