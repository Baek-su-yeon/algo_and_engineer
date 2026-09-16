def solution(participant, completion):
    hash_map = {}
    
    # 1. 참가자 명단을 해시에 기록 (이름: 인원수)
    for part in participant:
        if part in hash_map:
            hash_map[part] += 1
        else:
            hash_map[part] = 1
            
    # 2. 완주한 사람들의 명단을 해시에서 1씩 차감
    for comp in completion:
        hash_map[comp] -= 1
        
    # 3. 값이 0이 아닌(즉, 완주하지 못한) 단 한 명의 이름을 찾음
    for key, val in hash_map.items():
        if val > 0:
            return key


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])