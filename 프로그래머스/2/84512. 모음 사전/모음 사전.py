def solution(word):
    words = ['A','E','I','O','U']
    dictionary = set()

    def dfs(current):
        if 0 < len(current) <= 5:
            dictionary.add(current)
        if len(current) == 5:
            return
        for w in words:
            dfs(current + w)

    dfs("")
    dict_list = list(dictionary)
    dict_list.sort(key=lambda x: (x, len(x)))
    return dict_list.index(word) + 1 # 0-based