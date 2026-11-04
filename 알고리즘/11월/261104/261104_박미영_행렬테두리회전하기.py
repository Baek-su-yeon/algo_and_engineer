# rows x columns 크기인 행렬
# 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있음. 
# 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키고자 함.
# 각 회전은 (x1, y1, x2, y2)로 표현 : x1행 y1열부터 x2행 y2열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전 
# rows : 행 개수
# columns : 열 개수
# queries : 회전들의 목록 
# 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 출력 

def solution(rows, columns, queries):
    board = []
    answer = []
    
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(i * columns + j + 1)
        board.append(row)
        
    for query in queries:
        x1 = query[0] - 1
        y1 = query[1] - 1
        x2 = query[2] - 1
        y2 = query[3] - 1
        
        temp = board[x1][y1]
        min_num = temp
        
        # 윗면 (왼쪽 -> 오른쪽)
        for j in range(y1+1, y2+1):
            temp, board[x1][j] = board[x1][j], temp
            min_num = min(min_num, temp)
            
        # 오른쪽면 (위 -> 아래)
        for i in range(x1+1, x2+1):
            temp, board[i][y2] = board[i][y2], temp
            min_num = min(min_num, temp)
            
        # 아랫면 (오른쪽 -> 왼쪽)
        for j in range(y2-1, y1-1, -1):
            temp, board[x2][j] = board[x2][j], temp
            min_num = min(min_num, temp)
            
        # 왼쪽면 (아래 -> 위)
        for i in range(x2-1, x1-1, -1):
            temp, board[i][y1] = board[i][y1], temp
            min_num = min(min_num, temp)
            
        answer.append(min_num)
        
    return answer
