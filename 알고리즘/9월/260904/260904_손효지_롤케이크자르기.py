# def solution(topping):
#     # 공평하게 못나누면 0 출력하기
#     num_method = 0
#     for i in range(len(topping)):
#         older = topping[:i + 1]
#         younger = topping[i + 1:]
        
#         if len(set(older)) == len(set(younger)):
#             num_method += 1
                
#         else:
#             continue
    
#     answer = num_method
#     return print(answer)
# solution([1, 2, 1, 3, 1, 4, 1, 2])

# 위 코드는 시간초과. 다른 방법으로 접근하기... 

def solution(topping):
    n = len(topping)
    if n <= 1:
        return 0
    
    # 1. 왼족에서부터 각 위치까지의 '토핑 종류 수' 리스트 만들기
    left_distinct = [0] * n
    seen_left = set()
    for i in range(n):
        # 확인한 토핑 추가
        seen_left.add(topping[i])
        # 현재까지 확인된 토핑 개수 넣기
        left_distinct[i] = len(seen_left)
        
    right_distinct = [9] * n
    seen_right = set()
    
    # 오른쪽은 반대에서부터 시작
    for i in range(n - 1, -1, -1):
        seen_right.add(topping[i])
        right_distinct[i] = len(seen_right)
        
    num_method = 0
    
    for i in range(n - 1):
        # 왼, 오른쪽 토핑 개수가 같아지는 시점 확인
        if left_distinct[i] == right_distinct[i + 1]:
            num_method += 1
            
    return num_method