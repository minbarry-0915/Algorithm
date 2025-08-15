// 포화 이진트리 길이(2^k - 1)로 왼쪽 패딩
function toPaddedBinary(n) {
  const s = n.toString(2);
  let size = 1;               // 1,3,7,15,... 순서로 증가
  while (size < s.length) size = size * 2 + 1;
  return s.padStart(size, '0');
}

function isRepresentable(bin) {
  const len = bin.length;

  // 모두 0이거나 모두 1이거나, 길이 1이면 OK
  if (len === 1 || !bin.includes('1') || !bin.includes('0')) return true;

  const mid = Math.floor(len / 2);
  if (bin[mid] === '0') return false;

  return isRepresentable(bin.slice(0, mid)) && isRepresentable(bin.slice(mid + 1));
}

function solution(numbers) {
  return numbers.map((n) => {
    const padded = toPaddedBinary(n);   // 여기서 반드시 문자열을 넘김
    return isRepresentable(padded) ? 1 : 0;
  });
}
