def solution(board):
    o_count = sum(row.count('O') for row in board)
    x_count = sum(row.count('X') for row in board)

    # 턴 수 확인
    if not (o_count == x_count or o_count == x_count + 1):
        return 0

    def win(char):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == char:
                return True

        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] == char:
                return True

        if board[0][0] == board[1][1] == board[2][2] == char:
            return True

        if board[2][0] == board[1][1] == board[0][2] == char:
            return True

        return False

    o_win = win('O')
    x_win = win('X')

    # 0가 이기고 x도 턴 초과 안하고 제대로 뒀다면
    if o_win and o_count != x_count + 1:
        return 0

    # x가 이기고 x 턴 초과 안하고 제대로 뒀다면
    if x_win and o_count != x_count:
        return 0

    return 1