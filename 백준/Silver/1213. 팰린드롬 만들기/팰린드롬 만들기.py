import sys
from collections import Counter

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

def make_palindrome(word):
    # 문자의 개수가 짝수
    # 문자열의 길이가 홀수이면 한 종류의 문자만 홀수 개
    count = Counter(word)
    odd_count = 0
    odd_char = ''
    half = ''
    for ch in sorted(count.keys()):
        if count[ch] % 2 == 1: # 홀수개이면
            odd_count += 1
            odd_char = ch
        half += ch * (count[ch] // 2) # 절반만 더함

    if odd_count > 1:
        return "I'm Sorry Hansoo"

    return half + odd_char + half[::-1]


word = input().strip()
print(make_palindrome(word))