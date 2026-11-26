'''
정수집합 S 주어졌을 때
A이상 B 이하 모든 정수가 S에 속하지 않음

n을 포함하는 좋은 구간 A B의 개수
'''
'''
S 정렬해서
S의 원소 중
n이하의 최댓값 a
n이상의 최솟값 b

만약 n이 S에 포함된다면 답은 0
그 외에는 A는 a+1부터 n까지 가능
B는 n부터 b-1까지 가능


'''
L = int(input())
S = sorted(map(int, input().split()))
n = int(input())

a = 0
b = 0

if n in S:
    print(0)
else:
    for num in S:
        if num < n:
            a = num
        else:
            b = num
            break

    print((n - a) * (b - n) - 1)
        