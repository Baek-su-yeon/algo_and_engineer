from collections import deque

def solution(m, n, h, w, drops):
    inf = len(drops) + 1
    grid = [[inf] * n for _ in range(m)]

    for i, (r, c) in enumerate(drops):
        grid[r][c] = i + 1
            
    # 1. 가로 방향 슬라이딩 윈도우 (너비 w)
    row_min = [[0] * n for _ in range(m)]
    for r in range(m):
        dq = deque()
        for c in range(n):
            if dq and dq[0] <= c - w:
                dq.popleft()
                
            while dq and grid[r][dq[-1]] >= grid[r][c]:
                dq.pop()
            dq.append(c)
            row_min[r][c] = grid[r][dq[0]]
    
    # 2. 세로 방향 슬라이딩 윈도우 (높이 h) - 크기를 m x n으로 올바르게 수정
    col_min = [[0] * n for _ in range(m)]
    for c in range(w - 1, n):
        dq = deque()
        for r in range(m):
            if dq and dq[0] <= r - h:
                dq.popleft()
            while dq and row_min[dq[-1]][c] >= row_min[r][c]:
                dq.pop()
            dq.append(r)
            # [오타 수정] dq[0][c] -> row_min[dq[0]][c]
            col_min[r][c] = row_min[dq[0]][c]
            
    max_rain = -1
    best_r, best_c = 0, 0
    
    for r in range(h - 1, m):
        for c in range(w - 1, n):
            current_min = col_min[r][c]
            if current_min > max_rain:
                max_rain = current_min
                best_r = r - h + 1
                best_c = c - w + 1
    
    return [best_r, best_c]