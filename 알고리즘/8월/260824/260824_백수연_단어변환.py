from collections import deque

def is_change(now, compare):
    count = 0
    
    for i in range(len(now)):
        if now[i] != compare[i]:
            count += 1
        
        if 1 < count: return False
    
    if not count: return False

    return True
            

def solution(begin, target, words):
    
    used = [False] * len(words)
    
    q = deque()
    q.append((begin, 0))
    
    while q:
        now, count = q.popleft()
        
        if now == target:
            return count
        
        for i in range(len(words)):
            
            if not used[i] and is_change(now, words[i]):
                q.append((words[i], count + 1))
                used[i] = True
    
    return 0