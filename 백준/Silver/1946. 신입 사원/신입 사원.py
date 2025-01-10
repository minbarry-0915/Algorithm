import sys
input = sys.stdin.readline

T = int(input())
for test in range(T):
    n = int(input())

    applicants  = []
    for _ in range(n):
        doc_score, interview_score = map(int, input().split())
        applicants .append((doc_score, interview_score))

    applicants.sort()

    count = 1
    min_interview_score = applicants[0][1]

    for i in range(1, n):
        if applicants[i][1] < min_interview_score:
            count += 1
            min_interview_score = applicants[i][1]

    print(count)