parts = {
    1: [(0, 1), (0, -1)],
    2: [(-1, 0), (1, 0)],
    3: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    4: [(-1, 0), (0, -1)],
    5: [(-1, 0), (0, 1)],
    6: [(0, 1), (1, 0)],
    7: [(0, -1), (1, 0)]
}


def solution(grid):
    n, m = len(grid), len(grid[0])

    # 각 칸에서 이미 사용한 입구·출구 방향
    used = [[[] for _ in range(m)] for _ in range(n)]

    # 앞으로 통과해야 하는 기존 선로 횟수
    # 3번은 가로·세로를 각각 지나야 하므로 2회
    remaining = 0
    for row in grid:
        for value in row:
            if value == 3:
                remaining += 2
            elif value > 0:
                remaining += 1

    def dfs(si, sj, entry, remaining):
        if not (0 <= si < n and 0 <= sj < m):
            return 0

        current = grid[si][sj]

        if current == -1:
            return 0

        # 이미 사용한 입구로 다시 들어갈 수 없음
        if entry in used[si][sj]:
            return 0

        old = used[si][sj]
        opposite = (-entry[0], -entry[1])

        if current == 0:
            if not old:
                # 처음 방문한 빈칸:
                # 입구에 맞는 선로들의 출구를 후보로 저장
                candidates = []

                for number in (1, 2, 4, 5, 6, 7):
                    if entry in parts[number]:
                        for direction in parts[number]:
                            if direction != entry:
                                candidates.append(direction)

            else:
                # 이전에 직선으로 통과했는지 확인
                is_straight = (
                    len(old) == 2
                    and old[0] == (-old[1][0], -old[1][1])
                )

                if not is_straight:
                    return 0

                # 직선 선로를 수직 방향으로 재통과하면
                # 이 칸은 3번 교차 선로가 됨
                candidates = [opposite]

        elif current == 3:
            # 교차 선로에서는 직진
            candidates = [opposite]

        else:
            # 기존 선로에 해당 입구가 있어야 함
            if entry not in parts[current]:
                return 0

            candidates = [
                direction
                for direction in parts[current]
                if direction != entry
            ]

        answer = 0

        for out in candidates:
            # 이미 사용한 출구는 이용할 수 없음
            if out in old:
                continue

            # 이번에 사용한 입구·출구 기록
            used[si][sj] = old + [entry, out]

            left = remaining
            if current > 0:
                left -= 1

            if (si, sj) == (n - 1, m - 1):
                # 모든 기존 선로를 통과했을 때만 정답
                if left == 0:
                    answer += 1

            else:
                di, dj = out
                ni, nj = si + di, sj + dj

                answer += dfs(
                    ni, nj,
                    (-di, -dj),
                    left
                )

            # 다른 경로를 탐색하기 위해 복구
            used[si][sj] = old

        return answer

    # 시작점은 가로 방향으로 통과한 상태
    used[0][0] = parts[1][:]

    # 시작점 오른쪽 칸에 왼쪽 입구로 진입
    return dfs(0, 1, (0, -1), remaining - 1)