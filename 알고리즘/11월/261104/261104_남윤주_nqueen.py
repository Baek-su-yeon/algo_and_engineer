# x번째 행 문제 없는가
def is_promising(x):
    for i in range(x):
        # 서로 다른 행에서 퀸이 놓인 열이 달라야 함
        # 대각선으로도 놓일 수 없음
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

# x번째 행에 퀸 놓기
def n_queen(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queen(x+1)

 
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ans = 0
    row = [0] * n
    n_queens(0)
    print(f'#{tc} {ans}')