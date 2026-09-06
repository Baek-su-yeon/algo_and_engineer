from collections import deque

def solution(maps):
    n = len(maps[0])
    m = len(maps)
        
    dir = [(1,0), (-1,0), (0,-1), (0,1)]
    
    q = deque()
    visited = [[0] * n for _ in maps]
    
    q.append((0,0))
    visited[0][0] = 1
    
    while q:
        now = q.popleft()
        
        if now == (m - 1, n - 1):
            return visited[now[0]][now[1]]
        
        for y, x in dir:
            next = (now[0] + y, now[1] + x)
            
            if next[0] < 0 or m - 1 < next[0] or next[1] < 0 or n - 1 < next[1]:
                continue
                
            if maps[next[0]][next[1]] == 1 and not visited[next[0]][next[1]]:
                q.append(next)
                visited[next[0]][next[1]] = visited[now[0]][now[1]] + 1
    
    return -1