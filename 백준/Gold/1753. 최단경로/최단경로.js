class MinHeap {
	constructor() {
		this.heap = [];
	}

	size() {
		return this.heap.length;
	}

	swap(idx1, idx2) {
		[this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
	}

	heapPush(value) {
		this.heap.push(value);
		this.bubbleUp();
	}

	heapPop() {
		if (this.heap.length === 1) {
			return this.heap.pop();
		}

		const value = this.heap[0];
		this.heap[0] = this.heap.pop();
		this.bubbleDown();
		return value;
	}

	bubbleUp() {
		let index = this.heap.length - 1;
		let parentIdx = Math.floor((index - 1) / 2);
		while (
			this.heap[parentIdx] &&
			this.heap[index][0] < this.heap[parentIdx][0]
		) {
			this.swap(index, parentIdx);
			index = parentIdx;
			parentIdx = Math.floor((index - 1) / 2);
		}
	}

	bubbleDown() {
		let index = 0;
		let leftIdx = index * 2 + 1;
		let rightIdx = index * 2 + 2;

		while (
			(this.heap[leftIdx] && this.heap[leftIdx][0] < this.heap[index][0]) ||
			(this.heap[rightIdx] && this.heap[rightIdx][0] < this.heap[index][0])
		) {
			let smallerIdx = leftIdx;

			if (
				this.heap[rightIdx] &&
				this.heap[rightIdx][0] < this.heap[smallerIdx][0]
			) {
				smallerIdx = rightIdx;
			}

			this.swap(index, smallerIdx);
			index = smallerIdx;
			leftIdx = index * 2 + 1;
			rightIdx = index * 2 + 2;
		}
	}
}

const input = require("fs").readFileSync("/dev/stdin", "utf-8").split("\n");

const [v, e] = input[0].trim().split(" ").map(Number);
const start = Number(input[1]);

const graph = new Map();
for (let i = 2; i < e + 2; i++) {
	const [a, b, c] = input[i].trim().split(" ").map(Number);
	if (!graph.has(a)) {
		graph.set(a, []);
	}
	graph.get(a).push([b, c]);
}

const dist = Array(v + 1).fill(Infinity);
dist[start] = 0;
const heap = new MinHeap();
heap.heapPush([0, start]); // dist, idx

while (heap.size() > 0) {
	const [cost, curr] = heap.heapPop();

	const neighbors = graph.get(curr) || [];
	for (const [next, nextCost] of neighbors) {
		const totalCost = cost + nextCost;
		if (totalCost < dist[next]) {
			dist[next] = totalCost;
			heap.heapPush([totalCost, next]);
		}
	}
}

for (let i = 1; i < v + 1; i++) {
	if (dist[i] == Infinity) {
		console.log("INF");
	} else {
		console.log(dist[i]);
	}
}
