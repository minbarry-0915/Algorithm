function solution(priorities, location) {
    const queue = priorities.map((p, idx) => [p, idx]);
    let count = 0;

    while (queue.length > 0) {
        const [currentPriority, currentIndex] = queue.shift();

        const hasHigher = queue.some(([p, _]) => p > currentPriority);
        if (hasHigher) {
            queue.push([currentPriority, currentIndex]);
        } else {
            count++;
            if (currentIndex === location) {
                return count;
            }
        }
    }
}