# 배열의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수
# 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열 출력
# 뒷 큰수가 존재하지 않으면 -1을 담음. 

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = [0]
    
    for i in range(1, n):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack[-1]] = numbers[i]
            stack.pop()
        
        stack.append(i)
        
    return answer
