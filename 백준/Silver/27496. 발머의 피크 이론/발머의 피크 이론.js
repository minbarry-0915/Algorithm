const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

const [n, l] = input[0].trim().split(" ").map(Number);
const a = input[1].trim().split(" ").map(Number);

let current = 0;
let cnt = 0;

for (let i = 0; i < n; i++) {
	current += a[i];
	if (i >= l) current -= a[i - l];
	if (current >= 129 && current <= 138) cnt++;
}
console.log(cnt);
