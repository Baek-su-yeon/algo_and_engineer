def dfs(idx, total):
    global ans
    
    if total == K:
        ans += 1
        return
    
    if idx == N or total > K:
        return
    
    dfs(idx+1, total+A[idx])
    dfs(idx+1, total)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    ans = 0
    dfs(0, 0)
    
    print(f'#{tc} {ans}')