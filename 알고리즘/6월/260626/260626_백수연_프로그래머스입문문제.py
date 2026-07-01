# 문제 1.
# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = []
    
    for i in range(n + 1):
        if i % 2 != 0:
            answer.append(i)
            
    return answer

# 문제 2.
# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
def solution(n):
    answer = 0
    
    if n % 7 == 0: answer = n // 7
    else: answer = n // 7 + 1
    
    return answer

# 문제 3.
# 머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
import math

def gcd(n, num):
    while num != 0:
        n, num = num, n % num
    return n

def solution(n):
    answer = n // gcd(n, 6)
    
    answer = n // math.gcd(n, 6)
    
    return answer

# 문제 4
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = 0
    
    sum = 0
    
    for num in numbers:
        sum += num
        
    answer = sum / len(numbers)
    
    return answer