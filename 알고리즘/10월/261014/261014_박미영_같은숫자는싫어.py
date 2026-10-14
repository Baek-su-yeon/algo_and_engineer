# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
# 제거된 후 남은 수들을 반환할 때는 순서 유지

def solution(arr):
    answer = []
    
    n = -1 # 비교하는 숫자
    for i in range(len(arr)):
        if n == arr[i]:
            continue
        else:
            n = arr[i]
            answer.append(n)

    return answer

# 간결한 버전
def solution(arr):
    answer = []
    
    for n in arr:
        if not answer or answer[-1] != n:
            answer.append(n)
    
    return answer
