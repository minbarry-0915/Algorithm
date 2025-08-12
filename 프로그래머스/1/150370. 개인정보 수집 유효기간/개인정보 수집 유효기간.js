const getExpiredDate = (date, month) => {
    let d = new Date(date);
    d.setMonth(d.getMonth() + month);  
    d.setDate(d.getDate() - 1);        
    return d;
}

const isExpired = (target, today) => {
    return target < today;
}

function solution(today, terms, privacies) {
    const termsWithPeriod = {};
    const t = new Date(today);

    for (const term of terms){
        const [termName, period] = term.trim().split(' ');
        termsWithPeriod[termName] = parseInt(period);
    }

    const answer = [];

    privacies.forEach((privacy, idx) => {
        const [date, termName] = privacy.trim().split(' ');
        const period = termsWithPeriod[termName];
        const expiredDate = getExpiredDate(date, period);
        if (isExpired(expiredDate, t)) {
            answer.push(idx + 1);
        }
    });

    return answer;
}
