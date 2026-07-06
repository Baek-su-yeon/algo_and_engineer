# 문제 1
# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
def solution(numbers, direction):
    answer = []
    
    if direction == 'right':
        answer.append(numbers[-1])
        for i in range(len(numbers) - 1):
            answer.append(numbers[i])
    else:
        numbers.append(numbers[0])
        answer = numbers[1:]
    
    return answer

# 리스트컨프리헨션
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]

# rotate 함수
# deque.rotate(n): n이 양수면 오른쪽으로 회전, n이 음수면 왼쪽으로 회전
from collections import deque

def solution(numbers, direction):
    
    numbers = deque(numbers)
    
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    
    return list(numbers);