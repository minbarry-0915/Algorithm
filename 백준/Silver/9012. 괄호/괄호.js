const fs = require('fs');
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

T = parseInt(input[0], 10);
for (let i = 1; i <= T; i++) {
	const ps = input[i];
	const stack = [];
	let valid = true;

	for (token of ps) {
		if (token === '(') {
			stack.push(token);
		} else if (token === ')') {
			if (stack.length > 0 && stack[stack.length - 1] === '(') {
				stack.pop();
			} else {
				valid = false;
				break;
			}
		}
	}

	if (valid && stack.length === 0) {
		console.log('YES');
	} else {
		console.log('NO');
	}
}
