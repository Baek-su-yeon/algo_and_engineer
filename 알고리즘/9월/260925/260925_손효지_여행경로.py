def solution(tickets):
    answer = []
    n = len(tickets) + 1
    visited = [False] * n
    
    candidate = {}
    
    for i in range(n-1):
        dep = tickets[i][0]
        dest = tickets[i][1]
        
        if dep not in candidate:
            candidate[dep] = []
        candidate[dep].append(dest)
    
    for dep in candidate:
        candidate[dep].sort()
        
    def dfs(curr):
        while curr in candidate and candidate[curr]:  # candidate에 curr 키 있고, 비어있지 않다면
            next_dest = candidate[curr].pop(0)
            dfs(next_dest)
        answer.append(curr)
    dfs("ICN")
    return answer[::-1]
