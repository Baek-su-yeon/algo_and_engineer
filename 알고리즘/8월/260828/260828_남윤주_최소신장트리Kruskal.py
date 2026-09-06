'''
크루스칼
가중치가 가장 낮은 간선을 선택하며 찾아감
'''
 
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
 
def union(a, b):
    a = find(a)
    b = find(b)
 
    if a == b:
        return False
 
    if size[a] < size[b]:
        a, b = b, a
 
    parent[b] = a
    size[a] += size[b]
 
    return True
 
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
 
    edges = []
     
    for _ in range(E):
        a, b, w = map(int, input().split())
        edges.append((w, a, b))
 
    edges.sort()
 
    parent = [i for i in range(V+1)]
    size = [1] * (V+1)
 
    ans = 0
    cnt = 1
 
    for w, a, b in edges:
        if union(a, b):
            ans += w 
            cnt += 1
 
            if cnt == V:
                break
 
    print(f'#{tc} {ans}')