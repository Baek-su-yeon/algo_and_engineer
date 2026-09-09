# 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s
# s가 의미하는 원래 숫자 출력

def solution(s):
    number = {'zero':0, 'one':1, 'two':2, 'three':3,
             'four':4, 'five':5, 'six':6, 'seven':7,
             'eight':8, 'nine':9}
    
    for n in number:
        if n in s:
            s = s.replace(n, str(number[n]))
            
    return int(s)
