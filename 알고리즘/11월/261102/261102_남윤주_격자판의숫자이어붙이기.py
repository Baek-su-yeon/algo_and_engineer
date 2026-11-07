def dfs(x, y, num):
    if len(num) == 7:
        result.add(num)
        return
 
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
 
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, num + board[nx][ny])
 
 
T = int(input())
 
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
 
for tc in range(1, T + 1):
    board = [input().split() for _ in range(4)]
    result = set()
 
    for i in range(4):
        for j in range(4):
            dfs(i, j, board[i][j])
 
    print(f"#{tc} {len(result)}")
