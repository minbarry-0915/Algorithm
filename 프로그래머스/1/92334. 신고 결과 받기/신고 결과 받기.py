
def solution(id_list, report, k):
    user_report_record = {id: [] for id in id_list}
    reported_user = {id: 0 for id in id_list}
    for buffer in report:
        from_user, to_user = buffer.split()
        if to_user not in user_report_record[from_user]:
            user_report_record[from_user].append(to_user)
            reported_user[to_user] += 1
    banned_user = []
    for id, count in reported_user.items():
        if count >= k:
            banned_user.append(id)
    
    answer = []
    for id in id_list:
        report_record = user_report_record[id]
        count = 0
        for r in report_record:
            for b in banned_user:
                if r == b:
                    count += 1
        answer.append(count)
    return answer