const input = require("fs").readFileSync("/dev/stdin", "utf-8").split("\n");

const [n, k] = input[0].trim().split(" ").map(Number);
const dolls = input[1].trim().split(" ").map(Number);

let start = 0;
let end = 0;
let minLen = Infinity;
let cnt = 0;

while (true) {
	if (cnt >= k) {
		minLen = Math.min(minLen, end - start);
		if (dolls[start] === 1) {
			cnt--;
		}
		start++;
	} else if (end === n) {
		break;
	} else {
		if (dolls[end] === 1) {
			cnt++;
		}
		end++;
	}
}

if (minLen === Infinity) {
	console.log(-1);
} else {
	console.log(minLen);
}
