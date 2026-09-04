'''
회사에서 출발
N 고객 방문하고 집으로 돌아오는 최단 거리
 
visited 로 방문 관리
 
방문하지 않은 집들 중 하나 방문
방문 중 현재 최단 거리를 넘으면 중단
 
'''
# 현재 now번 집에 위치, 현재까지 이동 거리 dist, 현재까지 방문한 장소 수 cnt
def dfs(now, dist, cnt):
    global ans
 
    if dist >= ans:
        return
 
    if cnt == N:
        ans = min(ans, dist+ abs(locations[now * 2] - locations[2])+ abs(locations[now * 2 + 1] - locations[3]))
        return
 
    for nxt in range(2, N + 2):
        if not visited[nxt]:
            visited[nxt] = True
 
            nxt_dist = (abs(locations[now * 2] - locations[nxt * 2])+ abs(locations[now * 2 + 1] - locations[nxt * 2 + 1]))
 
            dfs(nxt, dist + nxt_dist, cnt + 1)
            visited[nxt] = False
 
 
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    locations = list(map(int, input().split()))
    visited = [False] * (N + 2)
    ans = float('inf')
 
    dfs(0, 0, 0)
 
    print(f"#{tc} {ans}")