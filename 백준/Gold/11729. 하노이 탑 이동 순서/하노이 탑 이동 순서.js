const input = require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim()
  .split('\n');

function hanolTower(n, start, end, result) {
  if (n === 1) {
    result.push(`${start} ${end}`);
    return;
  }

  const other = 6 - start - end;
  hanolTower(n - 1, start, other, result);
  result.push(`${start} ${end}`);
  hanolTower(n - 1, other, end, result);
}

const n = Number(input[0]);
const result = [];

console.log(2 ** n - 1);
hanolTower(n, 1, 3, result);
console.log(result.join('\n'));
