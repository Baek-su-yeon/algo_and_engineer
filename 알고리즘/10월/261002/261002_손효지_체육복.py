def solution(n, lost, reserve):
    # 여벌이 있지만 도난당한 학생은 양쪽 모두에서 제거
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    # 번호 순서대로 확인하기 위해 정렬 후 탐색
    for l in sorted(set_lost):
        if (l - 1) in set_reserve:
            set_reserve.remove(l - 1)
        elif (l + 1) in set_reserve:
            set_reserve.remove(l + 1)
        else:
            n -= 1
            
    return n