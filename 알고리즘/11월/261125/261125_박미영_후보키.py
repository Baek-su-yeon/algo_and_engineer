# 후보키 : 유일성과 최소성을 모두 만족 
# relation : 릴레이션을 나타내는 문자열 배열
# 릴레이션에서 후보키 개수 출력 

from itertools import combinations

def solution(relation):
    row = len(relation) # 행
    col = len(relation[0]) # 열 
    
    comb = []
    for i in range(1, col+1):
        comb.extend(combinations(range(col), i))
    
    unique = []
    for c in comb:
        values = set()
        for r in relation:
            temp = [r[i] for i in c]
            values.add(tuple(temp))
        
        if len(values) == row:
            minimal = True

            for key in unique:
                if set(key).issubset(set(c)):
                    minimal = False
                    break

            if minimal:
                unique.append(c)
                
    return len(unique)
