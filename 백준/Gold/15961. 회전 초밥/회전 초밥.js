const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

const [n, d, k, c] = input[0].split(' ').map(Number);
const belt = input.slice(1, n + 1).map(Number);

const counter = new Map();
let uniqueSushi = 0;
let max = 0; // 초밥 가짓수의 최댓값

// 윈도우 초기화
for (let i = 0; i < k; i++) {
	const sushi = belt[i];
	if (counter.has(sushi)) {
		counter.set(sushi, counter.get(sushi) + 1);
	} else {
		counter.set(sushi, 1);
		uniqueSushi++;
	}
}

max = counter.has(c) ? uniqueSushi : uniqueSushi + 1;

// 윈도우 루프 실행
for (let i = 1; i < n; i++) {
	const remove = belt[i - 1];
	const add = belt[(i + k - 1) % n];

	counter.set(remove, counter.get(remove) - 1);
	if (counter.get(remove) === 0) {
		counter.delete(remove);
		uniqueSushi--;
	}

	if (counter.has(add)) {
		counter.set(add, counter.get(add) + 1);
	} else {
		counter.set(add, 1);
		uniqueSushi++;
	}

	const total = counter.has(c) ? uniqueSushi : uniqueSushi + 1;
	max = Math.max(max, total);
}

console.log(max);
