from collections import deque # deque를 쓸거면

def solution(arr):
    answer = []
    answer_stack = deque() # deque를 쓸거면
    
    # for num in arr:
    #     if len(answer) == 0 or num != answer[-1]: answer.append(num)
        
    # 좀 더 파이썬 같이 풀려면
    # for num in arr:
    #     if not answer or num != answer[-1]: answer.append(num)
        
    # deque를 쓸거면
    for num in arr:
        if not answer_stack or num != answer_stack[-1]: answer_stack.append(num)
    answer = list(answer_stack)
    
    return answer