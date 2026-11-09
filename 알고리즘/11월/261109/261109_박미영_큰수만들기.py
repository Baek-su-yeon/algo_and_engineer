# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자 구하기
# number : 문자열 형식으로 주어지는 숫자
# k : 제거할 수의 개수 

# 숫자를 하나씩 확인하면서 이전에 선택한 숫자보다 크면, 이전의 작은 숫자를 제거

def solution(number, k):
    stack = []
    
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            k -= 1
            stack.pop()
        
        stack.append(num)
    
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)
