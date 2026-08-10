# 이중 for문
def solution(prices):
    answer = [] # 가격이 떨어지지 않은 기간을 담는 리스트
    
    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                if j == (len(prices) - 1):
                    answer.append(j - i)
                    break
                else:
                    continue
            else:
                answer.append(j - i)
                break
                
    answer.append(0)
    
    return answer

# 스택
def solution(prices):
    answer = [0] * len(prices) # 가격이 떨어지지 않은 기간을 담을 리스트
    stack = [] # 가격이 떨어지지 않은 초의 인덱스를 담을 스택
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            previous = stack.pop()
            answer[previous] = i - previous
        
        stack.append(i)
        
    while stack:
        previous = stack.pop()
        answer[previous] = len(prices) - 1 - previous
        
    return answer
