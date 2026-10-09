from collections import deque
import heapq

def solution(priorities, location):
    # 1. 실행 대기 큐 (원래 순서 유지)
    # [(2, 0), (1, 1), (3, 2), (2, 3)] 구조가 됩니다.
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    
    # 2. 우선순위만 모아둔 최대 힙 (현재 가장 높은 우선순위를 찾기 위함)
    max_heap = []
    for v in priorities:
        heapq.heappush(max_heap, -v)
        
    answer = 0  # 몇 번째로 실행되는지 세는 카운터
    
    while queue:
        # 큐에서 제일 앞의 프로세스를 꺼냅니다.
        current_v, current_i = queue.popleft()
        
        # 현재 힙의 최댓값(가장 높은 우선순위)과 비교합니다.
        if current_v < -max_heap[0]:
            # 뒤에 더 높은 우선순위가 있다면, 방금 꺼낸 걸 맨 뒤로 보냅니다.
            queue.append((current_v, current_i))
        else:
            # 내가 제일 높은 우선순위라면 실제로 '실행'합니다!
            answer += 1
            heapq.heappop(max_heap) # 실행했으니 힙에서도 제거합니다.
            
            # 실행한 프로세스가 내가 찾던 location의 프로세스라면 종료합니다.
            if current_i == location:
                return answer
