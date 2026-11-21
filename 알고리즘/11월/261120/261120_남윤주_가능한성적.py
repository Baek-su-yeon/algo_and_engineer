T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    total = {0}

    for score in scores:
        total |= {x + score for x in total}

    print(f'#{tc} {len(total)}')