const fs = require('fs');
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = parseInt(input[0], 10);

class Heap {
	constructor() {
		this.heap = [];
	}

	size() {
		return this.heap.length;
	}

	swap(x, y) {
		[this.heap[x], this.heap[y]] = [this.heap[y], this.heap[x]];
	}

	add(value) {
		this.heap.push(value);
		this.bubbleUp();
	}
	bubbleUp() {
		let idx = this.heap.length - 1;
		let parentIdx = Math.floor((idx - 1) / 2);

		while (parentIdx >= 0 && this.heap[idx] < this.heap[parentIdx]) {
			this.swap(idx, parentIdx);
			idx = parentIdx;
			parentIdx = Math.floor((idx - 1) / 2);
		}
	}
	poll() {
		if (this.heap.length === 1) {
			return this.heap.pop();
		}

		const val = this.heap[0];
		this.heap[0] = this.heap.pop();
		this.bubbleDown();
		return val;
	}

	bubbleDown() {
		let idx = 0;
		const length = this.heap.length;

		while (true) {
			let leftIdx = 2 * idx + 1;
			let rightIdx = 2 * idx + 2;
			let smallest = idx;

			if (leftIdx < length && this.heap[leftIdx] < this.heap[smallest]) {
				smallest = leftIdx;
			}

			if (rightIdx < length && this.heap[rightIdx] < this.heap[smallest]) {
				smallest = rightIdx;
			}

			if (smallest === idx) break;

			this.swap(idx, smallest);
			idx = smallest;
		}
	}
}

const heap = new Heap();

const results = [];
for (let i = 1; i <= n; i++) {
	const command = parseInt(input[i], 10);
	if (command > 0) {
		heap.add(command);
	} else {
		if (heap.size() === 0) {
			results.push('0');
		} else {
			results.push(heap.poll().toString());
		}
	}
}
console.log(results.join('\n'));
