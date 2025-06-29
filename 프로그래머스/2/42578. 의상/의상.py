def solution(clothes):
    from collections import defaultdict

    clothes_dict = defaultdict(list)

    for name, type in clothes:
        clothes_dict[type].append(name)

    answer = 1
    for type in clothes_dict:
        # 각 종류마다 (아이템 수 + 안 입는 경우 1)
        answer *= len(clothes_dict[type]) + 1

    return answer - 1  # 아무 것도 안 입는 경우 제외
    