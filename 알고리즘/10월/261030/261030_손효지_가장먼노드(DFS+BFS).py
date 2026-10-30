# import sys
# sys.setrecursionlimit(10**6)

# def find_child(curr, node_info, cnt):        
#     if curr in node_info:
#         for next_node in node_info[curr]:
#             if cnt[next_node] > cnt[curr] + 1:
#                 cnt[next_node] = cnt[curr] + 1
#                 find_child(next_node, node_info, cnt)


# def solution(n, vertex):
#     info = dict()
    
#     for v in vertex:
#         p, c = v[0], v[1]
#         if p not in info:
#             info[p] = []
#         info[p].append(c)
        
#         if c not in info:
#             info[c] = []
#         info[c].append(p)
#     cnt = [float('inf')] * (n + 1)
#     cnt[1] = 0
#     find_child(1, info, cnt)
    
#     valid_cnt = [c for c in cnt[1:] if c != float('inf')]
#     max_cnt = max(valid_cnt)
    
#     return cnt.count(max_cnt)

# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))


from collections import deque

def solution(n, vertex):
    info = dict()
    
    # 1. 양방향 인접 리스트 구성
    for v in vertex:
        p, c = v[0], v[1]
        if p not in info:
            info[p] = []
        info[p].append(c)
        
        if c not in info:
            info[c] = []
        info[c].append(p)
        
    cnt = [float('inf')] * (n + 1)
    cnt[1] = 0
    
    # 2. DFS(재귀) 대신 BFS(큐) 사용
    queue = deque([1])
    
    while queue:
        curr = queue.popleft()
        
        if curr in info:
            for next_node in info[curr]:
                if cnt[next_node] > cnt[curr] + 1:
                    cnt[next_node] = cnt[curr] + 1
                    queue.append(next_node)
                    
    # 3. 최대 거리 노드 개수 계산
    valid_cnt = [c for c in cnt[1:] if c != float('inf')]
    max_cnt = max(valid_cnt)
    
    return cnt.count(max_cnt)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 출력: 3