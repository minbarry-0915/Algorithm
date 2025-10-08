import sys
n,k = map(int,input().split())
order = list(map(int,input().split()))

plug = []
answer = 0
# 자리가 있으면 그냥 꽂는다
# 이미 꽂혀있으면 패스
# 자리가 없으면 뽑을거 고르기
# 앞으로 안쓸 에정이면 뽑기
# 모든게 다 쓰이면, 가장 나중에 다시 쓰이는 기기

for i in range(k):
    device = order[i]

    if device in plug:
        continue

    if len(plug) < n:
        plug.append(device)
        continue

    remove_target = -1
    farthest_idx = -1
    for p in plug:
        if p not in order[i + 1:]:
            remove_target = p
            break
        else:
            idx = order[i + 1:].index(p)
            if idx > farthest_idx:
                farthest_idx = idx
                remove_target = p

    plug.remove(remove_target)
    plug.append(device)
    answer += 1
print(answer)