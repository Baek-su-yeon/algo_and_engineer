# 컨테이너 벨트는 한 방향으로만 진행 가능해서 벨트에 놓인 순서대로(1번부터) 상자를 내릴 수 있음.
# 하지만 택배 기사님이 미리 알려준 순서에 맞게 영재가 택배상자를 실어야 함. 
# 만약 컨테이너 벨트의 맨 앞에 놓인 상자가 현재 트럭에 실어야 하는 순서가 아니라면
# 그 상자를 트럭에 실을 순서가 될 때까지 잠시 다른 곳에 보관해야 함. => 보조 컨테이너 벨트 추가 설치
# 보조 컨테이너 벨트는 가장 마지막에 보관한 상자부터 꺼냄.
# 보조로도 기사님 순서대로 못하면 더이상 상자를 싣지 않음.
# order : 택배 기사님이 원하는 상자 순서
# 영재가 몇 개의 상자를 실을 수 있는지 출력 

def solution(order):
    assist = [] # 보조 컨테이너 벨트
    
    i = 0 # order의 인덱스
    box = 1 # 지금 내려야 하는 박스의 번호
    turn = 1 # 컨테이너 몇 번째 보는지
    answer = 0 # 영재가 실을 수 있는 상자의 개수  
    while True:
        if assist and assist[-1] == order[i]:
            answer += 1
            i += 1
            assist.pop()
        else:
            if box > len(order):
                return answer
            
            if box == order[i]:
                answer += 1
                i += 1
                box += 1
            else:
                assist.append(box)
                box += 1
            
            
