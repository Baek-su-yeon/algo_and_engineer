# 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 함.
# 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하길 원함.
# k : 경화가 한 상자에 담으려는 귤의 개수
# tangerine : 귤의 크기를 담은 배열 
# 크기가 서로 다른 종류의 수의 최솟값 출력

def solution(k, tangerine):
    answer = 0 # 크기가 서로 다른 종류의 수
    size = {} # 크기 : 개수
    
    for t in tangerine:
        if t in size:
            size[t] += 1
        else:
            size[t] = 1
            
    size = sorted(size.values(), reverse=True)
    i = 0
    
    while k > 0:
        answer += 1
        k -= size[i]
        i += 1
        
    return answer
