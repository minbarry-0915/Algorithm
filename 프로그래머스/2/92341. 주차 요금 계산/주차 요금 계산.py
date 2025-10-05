import math
from collections import defaultdict

def solution(fees, records):
    base_time, base_fee, addition_time, addition_fee = map(int, fees)
    car_with_record = defaultdict(int)   # 차량별 입차 시간
    car_with_time = defaultdict(int)     # 차량별 누적 주차 시간
    
    def convert_minutes(time_str):
        hour, minute = map(int, time_str.split(':'))
        return hour * 60 + minute

    # 입출차 기록 처리
    for r in records:
        time_str, car_num, in_or_out = r.split()
        minutes = convert_minutes(time_str)

        if in_or_out == 'IN':
            car_with_record[car_num] = minutes
        else:  # OUT
            spent = minutes - car_with_record[car_num]
            car_with_time[car_num] += spent
            car_with_record[car_num] = -1  # 출차 처리

    # 출차하지 않은 차량 (23:59 출차 처리)
    for car_num, in_time in car_with_record.items():
        if in_time != -1:
            spent = convert_minutes("23:59") - in_time
            car_with_time[car_num] += spent

    # 요금 계산
    car_with_total_fee = {}
    for car_num in sorted(car_with_time.keys()):
        total_time = car_with_time[car_num]
        if total_time <= base_time:
            total_fee = base_fee
        else:
            total_fee = base_fee + math.ceil((total_time - base_time) / addition_time) * addition_fee
        car_with_total_fee[car_num] = total_fee
    print(car_with_total_fee)
    # 차량 번호 오름차순으로 결과 반환
    answer = [fee for _, fee in sorted(car_with_total_fee.items())]
    return answer
