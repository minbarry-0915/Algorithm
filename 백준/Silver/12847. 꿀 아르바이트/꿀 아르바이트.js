//const input = require("fs").readFileSync("input.txt", "utf-8").split("\n");
const input = require("fs").readFileSync("/dev/stdin", "utf-8").split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
const t = input[1].trim().split(" ").map(Number);

let start = 0;
let end = 0;
let max_pay = -1;

let prefix = [0];
for (let i = 0; i < n; i++) {
	prefix.push(prefix[i] + t[i]);
}

while (true) {
	if (end === n) {
		break;
	}
	if (end - start <= m) {
		const total = prefix[end] - prefix[start];
		max_pay = Math.max(max_pay, total);
		end++;
	} else {
		start++;
	}
}

console.log(max_pay);
