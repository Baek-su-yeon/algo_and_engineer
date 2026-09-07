def solution(queue1, queue2):
    sum1 = sum(queue1)
    total_sum = sum1 + sum(queue2)
    combined = queue1 + queue2
    n = len(queue1)

    # 짝수 아니라면 답을 찾을 수 없으니 -1 출력
    if total_sum % 2 != 0:
        return -1

    # 시작점
    p1 = 0
    # 끝 점
    p2 = n
    limit = n * 3
    answer = 0

    goal = total_sum // 2

    # 제한된 수 내에서 연산 시작
    while answer <= limit:
        if sum1 == goal:
            return answer
        # 아직 합이 큰 경우
        elif sum1 > goal:
            sum1 -= combined[p1]
            p1 = (p1 + 1) % len(combined)
        elif sum1 <= goal:
            sum1 += combined[p2]
            p2 = (p2 + 1) % len(combined)
        answer += 1
    return -1