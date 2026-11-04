from collections import deque

directions = [(0,1), (1,0), (0, -1), (-1, 0)]

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    def bfs(ci, cj):
        visited[ci][cj] = 1
        queue = deque([(ci, cj)])
        
        while queue:
            ti, tj = queue.popleft()
            
            if (ti, tj) == (n - 1, m - 1):
                return visited[ti][tj]
            
            for di, dj in directions:
                ni, nj = ti + di, tj + dj
                
                if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = visited[ti][tj] + 1
                    queue.append((ni, nj))
        # 도착 못하면 탐색 종료
        return -1
    
    return bfs(0,0)