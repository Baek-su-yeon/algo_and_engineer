from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for node in range(n):
        stack = deque()
        
        if not visited[node]:
            stack.append(node)
            
            while stack:
                now = stack.pop()
                
                if not visited[now]:
                    visited[now] = True
                
                    for idx in range(n):
                        connect = computers[now][idx]
                    
                        if connect and not visited[idx]:
                            stack.append(idx)
                        
            answer += 1
    
    return answer