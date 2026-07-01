# 문제 1.
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.
def solution(array):
    answer = 0
    
    counts = [0] * 1001
    
    for num in array:
        counts[num] += 1
        
    max_count = 0
    is_duplicated = False
    
    for i in range(1001):
        if max_count < counts[i]:
            is_duplicated = False
            max_count = counts[i]
            answer = i
        elif max_count == counts[i] and counts[i] != 0:
            is_duplicated = True
    
    if is_duplicated: return -1
    return answer

# 다른 방법
def solution(array):
    answer = 0
    counts = []
    
    for num in set(array): # set으로 중복제거
        counts.append((num, array.count(num)))
        
    max_count = max(count for num, count in counts)
    modes = [num for num, count in counts if count == max_count]
    return modes[0] if len(modes) == 1 else -1