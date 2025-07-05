function solution(progresses, speeds) {
    const remains = progresses.map((p) => 100 - p)
    
    const periods = remains.map((r,index) => Math.ceil(r / speeds[index]));
    
    const release = [];
    let current = periods[0];
    let count = 1;

    for (let i = 1; i < periods.length; i++) {
        if (periods[i] <= current) {
            count++;
        } else {
            release.push(count);
            current = periods[i];
            count = 1;
        }
    }
    release.push(count); // 마지막 그룹
    return(release)
}