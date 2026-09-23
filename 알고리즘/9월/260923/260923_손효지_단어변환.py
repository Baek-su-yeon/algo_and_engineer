def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = float('inf')
    visited = [False] * len(words)
    
    def dfs(current_word, count):
        nonlocal answer
    
        if current_word == target:
            answer = min(answer, count)
            return
        
        for i in range(len(words)):
            if not visited[i]:
                # 알파벳 1개만 차이나고, 아직 방문 안한 거 찾기...
                
                diff = 0
                for j in range(len(current_word)):
                    if current_word[j] != words[i][j]:
                        diff += 1
                        
                if diff == 1:  # 글자 1개 차이라면
                    visited[i] = True
                    dfs(words[i], count + 1)
                    visited[i] = False

    dfs(begin, 0)
    return answer if answer != float('inf') else 0