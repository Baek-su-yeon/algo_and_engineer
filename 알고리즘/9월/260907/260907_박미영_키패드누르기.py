# 맨 처음 왼손 엄지는 *, 오른손 엄지는 #에서 시작
# 엄지손가락은 상하좌우로만 이동 가능, 키패드 이동 한 칸은 거리 1
# 왼쪽 열의 1, 4, 7을 입력할 때는 왼손 엄지 사용
# 오른쪽 열의 3, 6, 9를 입력할 때는 오른손 엄지 사용
# 가운데 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드 위치에서 더 가까운 엄지 사용
# 만약 거리가 같다면 오른손잡이는 오른손 엄지, 왼손잡이는 왼손 엄지 
# numbers : 순서대로 누를 번호가 담긴 배열
# hand : 왼손잡이인지 오른손잡이인지 
# 각 번호를 누른 손가락이 왼손(L)인지 오른손(R)인지 연속된 문자열 형태로 출력 

def solution(numbers, hand):
    answer = '' # 각 번호를 누른 손가락들의 문자열
    
    keypad = {'1':[0,3], '2':[1,3], '3':[2,3],
             '4':[0,2], '5':[1,2], '6':[2,2],
             '7':[0,1], '8':[1,1], '9':[2,1],
             '*':[0,0], '0':[1,0], '#':[2,0]}
    
    cur_left = [0,0] # 왼손 현재 위치
    cur_right = [2,0] # 오른손 현재 위치 
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            cur_left = keypad[str(number)]
        elif number in [3, 6, 9]:
            answer += 'R'
            cur_right = keypad[str(number)]
        else:
            d_left = abs(keypad[str(number)][0] - cur_left[0]) + abs(keypad[str(number)][1] - cur_left[1])
            d_right = abs(keypad[str(number)][0] - cur_right[0]) + abs(keypad[str(number)][1] - cur_right[1])
            if d_left < d_right:
                answer += 'L'
                cur_left = keypad[str(number)]
            elif d_left > d_right:
                answer += 'R'
                cur_right = keypad[str(number)]
            else:
                if hand == 'left':
                    answer += 'L'
                    cur_left = keypad[str(number)]
                else:
                    answer += 'R'
                    cur_right = keypad[str(number)]
    return answer
                
                
        
    
