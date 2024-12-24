degrees = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

total_credit = 0
total_score = 0

for _ in range(20):
    subject = list(map(str,input().split()))
    if subject[2] != 'P':
        credit = float(subject[1])
        degree = degrees[subject[2]]
        total_credit += credit
        total_score += credit * degree

total_avg_degree = total_score / total_credit
print(total_avg_degree)