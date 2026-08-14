from collections import deque

def solution(n, computers):    
    # 아직 방문하지 않은, 연결된 다른 컴퓨터?
    visited = [0] * n
    
    def bfs(start):
        queue = deque([start])
        visited[start] = 1
        
        while queue:
            current = queue.popleft()
            
            for nxt in range(n):
                if (computers[current][nxt] == 1 and not visited[nxt]):
                    visited[nxt] = 1
                    queue.append(nxt)
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer