def get_day(date):
    yy,mm,dd = date.split('.')
    return int(dd) + int(mm)*28 + int(yy)*12*28

def solution(today, terms, privacies):
    today_days = get_day(today)
    
    terms_period_dict = {}
    for t in terms:
        term, expiration_period = t.split()
        terms_period_dict[term] = int(expiration_period) * 28
    
    answer = []
    for idx, p in enumerate(privacies):
        start, term_type = p.split()
        start_days = get_day(start)
        end_days = start_days + terms_period_dict[term_type] - 1
        if today_days > end_days:
            answer.append(idx + 1)
    
    return answer