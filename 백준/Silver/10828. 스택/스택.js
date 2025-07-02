const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = parseInt(input[0], 10);
const stack = [];
const result = [];

for (let i = 1; i <= n; i++) {
	const command = input[i].split(' ');

	switch (command[0]) {
		case 'push':
			stack.push(command[1]);
			break;

		case 'pop':
			result.push(stack.length !== 0 ? stack.pop() : -1);
			break;

		case 'size':
			result.push(stack.length);
			break;

		case 'empty':
			result.push(stack.length === 0 ? 1 : 0);
			break;

		case 'top':
			result.push(stack.length !== 0 ? stack[stack.length - 1] : -1);
			break;
	}
}

console.log(result.join('\n'));
