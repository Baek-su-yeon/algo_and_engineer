# 문제 1.
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = []
    
    # 방법 1.
    for num in numbers:
        answer.append(num * 2)
    
    # 방법 2. 리스트 컨프리헨션
    return [num * 2 for num in numbers] 
    return answer

# 문제 2.
# 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    answer = num1 % num2
    return answer

# 문제 3.
# 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.
def solution(array):
    answer = 0
    
    # 정렬(버블 정렬)
    # 헤깔리지 말 것, 제일 뒤부터 정렬된 값들이 쌓이니까 앞은 다 비교해야함
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    # 다른 풀이
    array.sort()
    
    # 중앙값
    answer = array[len(array) // 2]
    
    return answer