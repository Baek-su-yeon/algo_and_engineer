
T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrivals = sorted(map(int, input().split()))

    result = "Possible"

    for i in range(N):
        # i+1 번째 사람이 방문한 시각
        t = arrivals[i]
        # 해당 시각까지 생성된 붕어빵 개수
        produced = (t // M) * K
        # i+1 번째 사람이 방문했을 시각에 붕어빵 개수가 i+1보다 작다면 불가능
        if produced < i + 1:
            result = "Impossible"
            break

    print(f"#{tc} {result}")