# 입력받기
words = [input() for _ in range(5)]

# 결과 저장용 변수
result = ""

# 최대 단어 길이(최대 15자까지 주어질 수 있음)
max_length = max(len(word) for word in words)

# 세로로 읽기
for i in range(max_length):
    for word in words:
        if i < len(word):  # 단어의 현재 위치에 글자가 존재하면 추가
            result += word[i]

# 결과 출력
print(result)
