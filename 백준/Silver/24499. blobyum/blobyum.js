const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

const [n, k] = input[0].trim().split(" ").map(Number);
const sweetness = input[1].trim().split(" ").map(Number);

let currentSum = sweetness.slice(0, k).reduce((acc, curr) => acc + curr, 0);
let maxSum = currentSum;
for (let i = 0; i < n; i++) {
	currentSum = currentSum - sweetness[i] + sweetness[(i + k) % n];
	maxSum = Math.max(maxSum, currentSum);
}

console.log(maxSum);
