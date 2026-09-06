from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()    
    queue.append((0,0))

    while queue:
        # 큐에서 왼쪽값 먼저 꺼내서 스타트
        si, sj = queue.popleft()

        for d in range(4):
            ci, cj = si + dx[d], sj + dy[d]
            
            # 조건 만족하면
            if 0 <= ci < n and 0 <= cj < m and maps[ci][cj] == 1:
                # 이동 거리 증가
                maps[ci][cj] = maps[si][sj] + 1
                queue.append((ci, cj))
                
    answer = maps[n-1][m-1]
    return -1 if answer == 1 else answer