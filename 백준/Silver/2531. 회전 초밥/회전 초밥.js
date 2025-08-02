const input = require('fs')
	.readFileSync('/dev/stdin', 'utf-8')
	.trim()
	.split('\n');

// 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
const [n, d, k, c] = input[0].split(' ').map(Number);
const belt = input.slice(1, n + 1).map(Number);

const countMap = new Map();
let max = 0;
let uniqueCount = 0;

for (let i = 0; i < k; i++) {
	const sushi = belt[i];

	if (!countMap.has(sushi)) {
		uniqueCount++;
		countMap.set(sushi, 1);
	} else {
		countMap.set(sushi, countMap.get(sushi) + 1);
	}
}

max = countMap.has(c) ? uniqueCount : uniqueCount + 1;

for (let i = 1; i < n; i++) {
	const remove = belt[i - 1];
	const add = belt[(i + k - 1) % n];

	countMap.set(remove, countMap.get(remove) - 1);
	if (countMap.get(remove) === 0) {
		countMap.delete(remove);
		uniqueCount--;
	}

	if (!countMap.has(add)) {
		countMap.set(add, 1);
		uniqueCount++;
	} else {
		countMap.set(add, countMap.get(add) + 1);
	}

	const total = countMap.has(c) ? uniqueCount : uniqueCount + 1;
	max = Math.max(max, total);
}
console.log(max);
