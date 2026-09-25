# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줌.
# index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아감.
# skip에 있는 알파벳은 제외하고 건너뜀.

def solution(s, skip, index):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for sk in skip:
        alphabet.remove(sk)
        
    answer = ''
    
    for a in s:
        idx = alphabet.index(a)
        answer += alphabet[(idx + index) % len(alphabet)]
        
    return answer
        
        
