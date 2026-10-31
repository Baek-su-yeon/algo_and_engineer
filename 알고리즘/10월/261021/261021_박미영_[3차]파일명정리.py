# 단순한 문자 코드 순이 아닌, 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현
# 파일명은 100 글자 이내 : 영어 대소문자, 숫자, 공백, 마침표, 빼기 부호
# 영문자로 시작, 숫자 하나 이상 포함
# HEAD : 문자로 이루어짐, 최소한 한 글자 이상
# NUMBER : 한 글자에서 최대 다섯 글자 사이의 연속된 숫자, 양쪽에 0 가능
# TAIL : 나머지 부분, 숫자가 나타날 수도, 아무 글자도 없을 수도 있음.
# 우선 HEAD 부분을 기준으로 사전 순 정렬, 대소문자 구분 X
# HEAD가 같으면 NUMBER의 숫자 순으로 정렬
# HEAD랑 NUMBER가 같으면 원래 입력에 주어진 순서 유지 

def solution(files):
    answer = []
    
    for file in files:
        i = 0
        
        while not file[i].isdigit():
            i += 1
            
        head = file[:i]
        
        start = i
        while i < len(file) and i < start + 5 and file[i].isdigit():
            i += 1
            
        number = file[start:i]
        
        answer.append([file, head, number])
        
    answer_sorted = sorted(answer, key = lambda x : (x[1].lower(), int(x[2])))
    
    return [ans[0] for ans in answer_sorted]
