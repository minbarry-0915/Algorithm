T = int(input())

group_word_count = 0
for _ in range(T):
    word = str(input().strip())
    seen = set()
    is_group_word = True

    for i in range(len(word)):
        if word[i] in seen and word[i] != word[i - 1]:
            is_group_word = False
            break
        seen.add(word[i])

    if is_group_word:
        group_word_count += 1

print(group_word_count)