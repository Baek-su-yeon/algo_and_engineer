# fees : 주차 요금을 나타내는 정수 배열, [기본 시간, 기본 요금, 단위 시간, 단위 요금]
# records : 자동차의 입/출차 내역을 나타내는 문자열 배열, [시각, 차량 번호, 내역]
# 누적 주차 시간이 기본 시간 이하라면, 기본 요금 청구
# 누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해서 초과한 시간에 대한 단위 시간마다 단위 요금 청구
# 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면 올림
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 출력

import math

def solution(fees, records):
    parking = {} # 차량별 주차 시간
    answer = {} # 차량별 요금
    in_cars = set() # 입차 차량
    
    for record in records:
        time, number, state = record.split(" ") # 시각, 차량번호, 내역
        hour, minute = time.split(":") # 시, 분
        minute_park = int(hour) * 60 + int(minute) # 시각을 분으로 바꿈.
        
        if number not in parking:
            parking[number] = []
        
        if state == "IN":
            parking[number].append(minute_park)
            in_cars.add(number)
        else:
            parking[number][-1] = minute_park - parking[number][-1]
            in_cars.remove(number)
            
    for number in parking:
        if number in in_cars:
            parking[number][-1] = 1439 - parking[number][-1]
            
        total_park = sum(parking[number])
            
        if total_park <= fees[0]:
            answer[number] = fees[1]
        else:
            answer[number] = fees[1] + math.ceil((total_park - fees[0])/fees[2]) * fees[3]
                
    return [answer[number] for number in sorted(answer)]
