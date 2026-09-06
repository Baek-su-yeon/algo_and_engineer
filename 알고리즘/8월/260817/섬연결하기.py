def solution(n, costs):
    # 1. 비용을 기준으로 간선 오름차순 정렬 (그리디의 시작)
    costs.sort(key=lambda x: x[2])
    
    # 2. Union-Find를 위한 부모 테이블 초기화
    parent = [i for i in range(n)]
    
    def find(parent, i):
        if parent[i] == i:
            return i
        parent[i] = find(parent, parent[i])
        return parent[i]

    def union(parent, i, j):
        root_i = find(parent, i)
        root_j = find(parent, j)
        if root_i < root_j:
            parent[root_j] = root_i
        else:
            parent[root_i] = root_j

    min_cost = 0
    edge_count = 0
    
    # 3. 비용이 작은 간선부터 하나씩 확인
    for edge in costs:
        u, v, cost = edge
        # 사이클이 발생하지 않는 경우에만 선택 (Union)
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            min_cost += cost
            edge_count += 1
            if edge_count == n - 1:
                break
                
    return min_cost