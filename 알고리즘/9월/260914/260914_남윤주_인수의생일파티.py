'''
각 점에서 X까지의 거리와 X에서 각 점까지의 최단 거리
 
모든 간선은 단방향
'''
import heapq
 
INF = float('inf')
 
def dijkstra(start, graph, N):
    dist = [INF] * (N + 1)
    dist[start] = 0
 
    pq = [(0, start)]
 
    while pq:
        cur_dist, cur = heapq.heappop(pq)
 
        if cur_dist > dist[cur]:
            continue
 
        for nxt, cost in graph[cur]:
            new_dist = cur_dist + cost
 
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))
 
    return dist
 
 
T = int(input())
 
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
 
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]
 
    for _ in range(M):
        x, y, c = map(int, input().split())
 
        graph[x].append((y, c))
        reverse_graph[y].append((x, c))
 
    from_x = dijkstra(X, graph, N)
 
    to_x = dijkstra(X, reverse_graph, N)
 
    answer = 0
 
    for i in range(1, N + 1):
        answer = max(answer, from_x[i] + to_x[i])
 
    print(f"#{tc} {answer}")