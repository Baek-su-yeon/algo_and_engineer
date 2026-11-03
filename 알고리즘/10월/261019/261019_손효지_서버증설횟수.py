def solution(players, m, k):
    count = 0
    n = len(players)
    
    # 각 시간대별로 만료되는 서버의 개수를 저장하는 배열
    expiry = [0] * (n + k)
    current_servers = 0
    
    for i in range(n):
        # 1. 현재 시간에 만료되는 서버를 현재 서버 수에서 제외
        current_servers -= expiry[i]
        
        # 2. 현재 필요한 서버 수 계산
        required = players[i] // m
        
        # 3. 현재 서버가 부족하다면 추가 증설
        if current_servers < required:
            needed = required - current_servers
            count += needed
            current_servers += needed
            # k시간 뒤에 만료되도록 기록
            expiry[i + k] += needed
            
    return count