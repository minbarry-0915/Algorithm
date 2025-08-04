const input = require("fs").readFileSync("/dev/stdin", "utf-8").split("\n");

const [n, k] = input[0].trim().split(" ").map(Number);
const namesLength = [];

for (let i = 1; i < n + 1; i++) {
	const len = input[i].trim().length;
	namesLength.push(len);
}

const lengthQueues = new Map();
let answer = 0;

for (let i = 0; i < n; i++) {
	const len = namesLength[i];
	if (!lengthQueues.has(len)) {
		lengthQueues.set(len, []);
	}
	q = lengthQueues.get(len);

	while (q.length > 0 && i - q[0] > k) {
		q.shift();
	}

	answer += q.length;
	q.push(i);
}
console.log(answer);
