const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

const [n, k] = input[0].trim().split(" ").map(Number);
const MAXPOS = 1000001;
const x = new Array(MAXPOS).fill(0);

for (let j = 1; j < n + 1; j++) {
	const [g, i] = input[j].trim().split(" ").map(Number);
	x[i] = g;
}

const windowSize = 2 * k + 1; // 양쪽 k개, 나

let currentSum = x.slice(0, windowSize).reduce((a, b) => a + b, 0);
let maxIce = currentSum;

for (let i = windowSize; i < MAXPOS; i++) {
	currentSum = currentSum - x[i - windowSize] + x[i];
	maxIce = Math.max(maxIce, currentSum);
}

console.log(maxIce);
