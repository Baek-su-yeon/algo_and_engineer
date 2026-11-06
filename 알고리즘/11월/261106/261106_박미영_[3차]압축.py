# 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화 
# 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾음.
# 3. w에 해당하는 사전의 색인 번호 출력, 입력에서 w 제거
# 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록
# 5. 단계 2로 돌아감.
# msg : 영문 대문자로만 이뤄진 문자열 
# 주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력 

def solution(msg):
    dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
          'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,
          'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    
    answer = []
    last = 27
    
    while len(msg) >= 1:
        for i in range(1, len(msg)+1):
            s = msg[:i]
            if s not in dic:
                dic[s] = last
                answer.append(dic[s[:-1]])
                msg = msg[i-1:]
                last += 1
                break
        else:
            answer.append(dic[msg])        
            break
                
    return answer 
