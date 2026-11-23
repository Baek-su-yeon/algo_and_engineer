# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수 찾기
# 문자열로 출력 

def solution(numbers):
    numbers = [str(number) for number in numbers]
    numbers.sort(key=lambda x:x*4, reverse=True)
    
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    else:
        return answer
