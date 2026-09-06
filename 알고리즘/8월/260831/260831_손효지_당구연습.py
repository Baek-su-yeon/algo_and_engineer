def solution(m, n, startX, startY, balls):
    answer = []

    for target in balls:
        targetX, targetY = target[0], target[1]
        min_dist = float('inf')

        # 1. 왼쪽 쿠션 (x = 0)
        # 조건: 시작점과 공의 y 좌표가 같고, 공이 왼쪽에 있다면 쿠션보다 직접 치는 것이 먼저이므로 제외
        if not (startY == targetY and targetX < startX):
            dx = targetX - (-startX)
            dy = targetY - startY
            min_dist = min(min_dist, dx ** 2 + dy ** 2)

        # 2. 오른쪽 쿠션 (x = m)
        # 조건: 시작점과 공의 y 좌표가 같고, 공이 오른쪽에 있다면 제외
        if not (startY == targetY and targetX > startX):
            dx = targetX - (2 * m - startX)
            dy = targetY - startY
            min_dist = min(min_dist, dx ** 2 + dy ** 2)

        # 3. 아래쪽 쿠션 (y = 0)
        # 조건: 시작점과 공의 x 좌표가 같고, 공이 아래쪽에 있다면 제외
        if not (startX == targetX and targetY < startY):
            dx = targetX - startX
            dy = targetY - (-startY)
            min_dist = min(min_dist, dx ** 2 + dy ** 2)

        # 4. 위쪽 쿠션 (y = n)
        # 조건: 시작점과 공의 x 좌표가 같고, 공이 위쪽에 있다면 제외
        if not (startX == targetX and targetY > startY):
            dx = targetX - startX
            dy = targetY - (2 * n - startY)
            min_dist = min(min_dist, dx ** 2 + dy ** 2)

        answer.append(min_dist)

    return answer