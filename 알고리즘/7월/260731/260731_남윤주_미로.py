'''
출발점에서 도착지점까지 가는 길 존재 여부
'''
from collections import deque

def bfs(x, y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    queue = deque([(x, y)])
    
    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if (0 <= nx < 16) and (0 <= ny < 16):

                if board[nx][ny] == 3:
                    return 1
                    
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    queue.append((nx, ny))
    return 0

    
for _ in range(1, 11):
    tc = int(input())
    board = [list(map(int, input())) for i in range(16)]

    sx = sy = 0
    is_find = False
    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                sx = i
                sy = j
                is_find = True
                break
        if is_find:
            break
                
    ans = bfs(sx, sy)
    print(f'#{tc} {ans}')
    