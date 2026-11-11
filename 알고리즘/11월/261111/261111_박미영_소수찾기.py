# 한자리 숫자가 적힌 조이 조각이 흩어져있음.
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는가
# numbers : 각 종이 조각에 적힌 숫자가 적힌 문자열

from itertools import permutations

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers)+1):
        per = permutations(numbers, i)
        
        for p in per:
            num = int(''.join(p))
            
            if num < 2:
                continue
                
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break
            else:
                answer.add(num)

    return len(answer)
