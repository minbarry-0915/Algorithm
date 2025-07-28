def is_palindrome(word, start, end):
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

def is_pseudo_palindrome(word):
    start = 0
    end = len(word) - 1

    while start < end:
        if word[start] != word[end]:
            return is_palindrome(word, start + 1, end) or is_palindrome(word, start, end - 1)
        start += 1
        end -= 1
    return True


T = int(input())
for _ in range(T):
    word = list(input())
    if is_palindrome(word, 0, len(word) - 1):
        print(0)
    elif is_pseudo_palindrome(word):
        print(1)
    else:
        print(2)