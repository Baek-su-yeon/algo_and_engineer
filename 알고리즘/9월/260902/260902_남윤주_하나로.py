T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
 
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
 
    E = float(input())
 
    INF = float('inf')
 
    min_dist = [INF] * N
     
    visited = [False] * N
 
    min_dist[0] = 0
 
    total = 0
 
    for _ in range(N):
        now = -1
        min_value = INF
 
        for i in range(N):
            if not visited[i] and min_dist[i] < min_value:
                min_value = min_dist[i]
                now = i
 
        visited[now] = True
        total += min_dist[now]
 
        for next in range(N):
            if not visited[next]:
                dx = x[now] - x[next]
                dy = y[now] - y[next]
 
                dist = dx * dx + dy * dy
 
                if dist < min_dist[next]:
                    min_dist[next] = dist
 
    answer = round(total * E)
 
    print(f"#{tc} {answer}")