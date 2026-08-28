'''
Prim
인접 정점 중 가중치가 낮은 정점을 찾아 넣음
사이클이 생기지 않도록 유의
 
 
가장 가중치가 작은 간선부터 확인해야 함
>> heap을 이용 (간선 길이, 정점)
 
모든 노드가 이어져있는지 확인을 위해 visited 이용
'''
from heapq import heappush, heappop
 
def prim(start):
    pq = [(0, start)]
    visited = [False] * (V+1)
 
    total_cost = 0
    count = 0
 
    while pq:
        # 간선 제일 짧은 것 꺼냄
        cost, now_node = heappop(pq)
 
        # 방문한 적 있다면 패스
        if visited[now_node]:
            continue
 
        visited[now_node] = True
        total_cost += cost
        count += 1
 
        if count == V:
            return total_cost
             
        for nxt_node, nxt_cost in graph[now_node]:
            if not visited[nxt_node]:
                heappush(pq, (nxt_cost, nxt_node))
 
    return
             
     
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
     
    # 인접노드 관리 (인접노드, 가중치)
    graph = [[] for _ in range(V+1)]
     
    for _ in range(E):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
 
    answer = prim(1)
 
    print(f'#{tc} {answer}')