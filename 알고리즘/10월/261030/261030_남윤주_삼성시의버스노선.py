'''
5000개 버정
노선은 N개 
 
i번째 노선은 번호가 Ai 이상 Bi 이하인 정류장만을 다님
 
P개의 정류장 번호가 주어질 때 해당 번호의 정류장을 지나는 노선의 가짓수
 
x번 정류장을 지나는 노선의 총 개수는 어떻게 구할 수 있을까
노선은 최대 500개밖에 없음.
'''
'''
노선이 시작되는 지점과 끝나는 지점 관리하여 해당 정류장 지나는 노선 개수 카운트
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5002
 
    for _ in range(N):
        a, b = map(int, input().split())
        # a를 지나는 노선 개수 추가
        counts[a] += 1
        # 앞서 시작한 노선이 끝남
        counts[b+1] -= 1
 
    # i번 정류장을 지나는 노선의 개수
    for i in range(1, 5001):
        counts[i] += counts[i-1]
 
    P = int(input())
    ans = []
    for _ in range(P):
        c = int(input())
        ans.append(counts[c])
 
    print(f'#{tc}', *ans)