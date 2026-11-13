# 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로
# 만들 수 있는 수가 모두 몇 가지인가 
# elements : 원형 수열의 모든 원소 

def solution(elements):
    answer = set()
    
    n = len(elements)
    for i in range(1, n+1): # 부분 수열의 길이
        part = sum(elements[:i])
        for j in range(n): # 부분 수열의 시작 위치
            # j에서 시작해서 i개의 원소
            # 선택한 원소들의 합 계산
            part = part - elements[j] + elements[(j + i) % n]
            answer.add(part)
            
    return len(answer)
