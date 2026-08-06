from collections import deque

def solution(s):
    answer = True
    
    stack = deque()
    stack.append(s[0])
    
    for i in range(1, len(s)):
        
        if not stack:
            stack.append(s[i])
            continue
        
        prev = stack[-1]
        
        if prev == s[i]:
            stack.append(s[i])
            
        elif prev == '(' and s[i] == ')':
            stack.pop()
            
    if not stack:
        return True
    else:
        return False