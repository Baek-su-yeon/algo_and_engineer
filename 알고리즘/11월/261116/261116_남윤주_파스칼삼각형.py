'''
파스칼 삼각형의 각 층
nC0 부터 nCn까지
0C0
1C0 1C1
2C0 2C1 2C2
'''
'''
실제 combination을 계산해도 되고
윗 층의 값을 활용해 아래 층을 계산해도 되고
전부 미리 만들어놓고 출력해도 되고
대칭성을 활용해도 되고
'''

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    # 총 층
    N = int(input())
    prev = [1] * N
    # 각 층을 출력
    for i in range(N):
        arr = [1] * (i + 1)
        for j in range(1, i):
            arr[j] = prev[j-1] + prev[j]

        prev = arr
        print(*arr)



