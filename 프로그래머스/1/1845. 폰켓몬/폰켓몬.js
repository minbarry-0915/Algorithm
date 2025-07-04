function solution(nums) {
    const n = nums.length;
    const unique = new Set(nums);
    
    return (Math.min(unique.size, Math.floor(n / 2)))
}