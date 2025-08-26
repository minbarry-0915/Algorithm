function solution(survey, choices) {
    const scores = [0,3,2,1,0,1,2,3]

    const typeScores = {
      R: 0,
      T: 0,
      C: 0,
      F: 0,
      J: 0,
      M: 0,
      A: 0,
      N: 0,
    }
    
    for (let i = 0; i < choices.length; i ++){
        const s = survey[i]
        const c = choices[i]
        if (1 <= c && c <= 3){
            typeScores[s[0]] += scores[c]
        }else if(5 <= c && c <= 7){
            typeScores[s[1]] += scores[c]
        }
    }

    const result = [
        typeScores['R'] >= typeScores['T'] ? 'R' : 'T',
        typeScores['C'] >= typeScores['F'] ? 'C' : 'F',
        typeScores['J'] >= typeScores['M'] ? 'J' : 'M',
        typeScores['A'] >= typeScores['N'] ? 'A' : 'N'
    ].join('');

    return result
}