# 각 종류별로 최대 1가지 의상만 착용 가능
# 착용한 의상의 일부가 겹쳐도 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법
# 하루에 최소 한 개의 의상은 입음.
# clothes : 코니가 가진 의상들이 담긴 2차원 배열, [의상 이름, 의상 종류]
# 서로 다른 옷의 조합의 수 출력 

def solution(clothes):
    cloth_type = {}
    
    for cloth in clothes:
        if cloth[1] not in cloth_type:
            cloth_type[cloth[1]] = 0
        
        cloth_type[cloth[1]] += 1
    
    answer = 1
    for cnt in cloth_type.values():
        answer *= (cnt + 1)
        
    return answer - 1
