'''
높이가 B인 선반
N명 점원
키 Hi
점원들이 탑을 쌓아서 선반 위의 물건을 꺼냄. 
'''
'''
가능한 모든 경우를 탐색
B가 되면 결과 내고 종료
B 이상이면 해당 케이스는 탐색 중단 & 답 개선
'''
# x번째 수, 현재 합
def dfs(x, now):
    global ans
    
    if now >= B:
        ans = min(ans, now)
        return
    if x == N:
        return
    
    dfs(x+1, now + heights[x])
    dfs(x+1, now)
    
    
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    ans = 200002
    dfs(0, 0)
    print(f'#{tc} {ans-B}')
    