# 숫자나라 기사단 : 1 ~ number까지 번호 지정
# 각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려 함.
# 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가지는 무기를 구매해야 함.
# 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요
# 무기점에서 무기를 모두 만들기 위해 필요한 철의 무게 계산
# number : 기사단원의 수
# limit : 이웃나라와 협약으로 정해진 공격력의 제한수치
# power : 제한수치를 초과한 기사가 사용할 무기의 공격력 

def solution(number, limit, power):
    answer = 0 # 무기를 모두 만들기 위해 필요한 철의 무게
    
    for n in range(1, number + 1):
        divisor = 0 # 약수의 개수
        
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if i * i == n:
                    divisor += 1
                else:
                    divisor += 2
            
            if divisor > limit:
                break
        
        if divisor > limit:
            answer += power
        else:
            answer += divisor
            
    return answer
