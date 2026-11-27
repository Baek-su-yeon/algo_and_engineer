# 대기실은 5개, 각 행이 대기실 
# 거리두기를 위하여 응시자들끼리는 맨해튼 거리가 2 이하로 앉으면 안 됨.
# 응시자 사이에 파티션으로 막혀 있으면 허용
# P : 응시자가 앉아있는 자리
# O : 빈 테이블
# X : 파티션
# 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 출력

from itertools import combinations

def solution(places):
    answer = []
    
    for place in places:
        result = 1 # 일단 거리두기를 준수한다고 가정
        # 응시자 찾기
        person = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    person.append([i, j])
                    
        for a, b in combinations(person, 2): # 응시자 두 명씩 뽑아서
            man = abs(a[0] - b[0]) + abs(a[1] - b[1]) # 맨해튼 거리
            
            if man == 1: # 무조건 위반
                result = 0
                break
            elif man == 2 and a[0] == b[0]:
                mid = (a[1] + b[1]) // 2
                if place[a[0]][mid] != "X":
                    result = 0
                    break
            elif man == 2 and a[1] == b[1]:
                mid = (a[0] + b[0]) // 2
                if place[mid][a[1]] != "X":
                    result = 0
                    break
            elif man == 2 and abs(a[0]-b[0]) == 1 and abs(a[1]-b[1]) == 1:
                if place[a[0]][b[1]] != "X" or place[b[0]][a[1]] != "X":
                    result = 0
                    break
            
        answer.append(result)
        
    return answer
             

                
