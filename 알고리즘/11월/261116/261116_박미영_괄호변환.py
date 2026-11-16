# 균형잡힌 괄호 문자열 : '('의 개수와 ')'의 개수가 같은 경우
# 올바른 괄호 문자열 : '('와 ')'의 괄호의 짝도 모두 맞을 경우 
# 균형잡힌 괄호 문자열 p가 주어질 때, 올바른 괄호 문자열로 변환

def solution(p):
    answer = ""
    
    if len(p) == 0:
        return p
    else:
        u = ""
        v = ""
        left_s = 0
        right_s = 0
        correct = True # 올바른 괄호 문자열인가
        
        for s in p:
            if s == "(":
                left_s += 1
            else:
                right_s += 1
                
            if right_s > left_s:
                correct = False
            
            if left_s == right_s:
                u = p[:(left_s + right_s)]
                v = p[(left_s + right_s):]
                break
                
        if correct:
            return u + solution(v)
        else:
            answer = "(" + solution(v) + ")"
            
            for s in u[1:-1]:
                if s == "(":
                    answer += ")"
                else:
                    answer += "("
                    
    return answer
