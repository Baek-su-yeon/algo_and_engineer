# 네 가지 발음과 그걸 조합해서 만들 수 있는 발음밖에 하지 못함.
# 연속해서 같은 발음 하는 거 어려워함.
# babbling : 문자열 배열
# 발음할 수 있는 단어의 개수 

def solution(babbling):
    can = ["aya", "ye", "woo", "ma"] # 발음할 수 있는 거
    answer = 0 # 발음할 수 있는 단어의 개수
    
    for b in babbling:
        possible = True
        for c in can:
            if 2 * c in b: # 2번 연속되는 것만 찾아도 발음 못 하는 거임
                possible = False
                break
        
        if possible:
            for c in can:
                b = b.replace(c, 'X')
        else:
            continue
        
        count = b.count('X')    
        if count == len(b):
            answer += 1
    
    return answer
        
        
