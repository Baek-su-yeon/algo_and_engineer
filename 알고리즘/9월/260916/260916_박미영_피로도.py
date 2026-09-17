# 최소 필요 피로도 : 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
# 소모 피로도 : 던전을 탐험한 후 소모되는 피로도 
# 한 유저가 던전을 최대한 많이 탐험하려 함.
# k : 유저의 현재 피로도
# dungeons : 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 
# 유저가 탐험할 수 있는 최대 던전 수 

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for order in permutations(dungeons):
        fatigue = k
        count = 0
        
        for required, cost in order:
            if fatigue >= required:
                fatigue -= cost
                count += 1
                
        answer = max(answer, count)
        
    return answer
