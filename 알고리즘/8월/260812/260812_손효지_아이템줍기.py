from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 1. 좌표를 2배로 확장 (50 -> 최대 100, 여유 있게 102x102 크기 배열 사용)
    max_size = 102
    board = [[-1] * max_size for _ in range(max_size)]
    
    # 2. 사각형 내부를 채우고, 테두리만 남기기
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                # 테두리인 경우 (이미 내부로 처리된 적이 없다면 1로 설정)
                if x == x1 or x == x2 or y == y1 or y == y2:
                    if board[x][y] != 0:
                        board[x][y] = 1
                # 사각형 내부인 경우 0으로 채움
                else:
                    board[x][y] = 0

    # 3. BFS를 위한 준비 (시작점과 아이템 위치도 2배 확대)
    start_x, start_y = characterX * 2, characterY * 2
    target_x, target_y = itemX * 2, itemY * 2
    
    queue = deque([(start_x, start_y)])
    visited = [[1] * max_size for _ in range(max_size)]
    visited[start_x][start_y] = 0
    
    # 상, 하, 좌, 우 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 4. BFS 탐색 실행
    while queue:
        x, y = queue.popleft()
        
        # 목적지에 도달했다면 이동 거리 반환 (2배로 늘렸으므로 최종 거리를 2로 나눔)
        if x == target_x and y == target_y:
            return visited[x][y] // 2
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 다음 좌표가 테두리(1)이고 아직 방문하지 않았다면
            if board[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return 0