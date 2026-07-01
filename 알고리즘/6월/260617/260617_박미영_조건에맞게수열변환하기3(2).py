def solution(arr, k):
    if k % 2:
        return [n * k for n in arr]
    return [n + k for n in arr]
