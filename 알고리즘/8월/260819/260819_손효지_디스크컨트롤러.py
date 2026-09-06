import heapq

def solution(jobs):
    # 1. 작업 요청 시각을 기준으로 오름차순 정렬
    jobs.sort(key=lambda x: x[0])
    
    current_time = 0  # 현재 시간
    total_turnaround_time = 0  # 각 작업의 (종료 시각 - 요청 시각)의 총합
    i = 0  # jobs 배열을 가리키는 인덱스
    start = -1  # 마지막에 완료된 작업의 시작 시각 (또는 직전에 끝난 시각)
    
    hq = []  # 소요 시간 기준 최소 힙
    
    # 모든 작업을 처리할 때까지 반복
    while i < len(jobs) or hq:
        # 현재 시점까지 들어온 모든 작업들을 힙에 넣기
        # 힙에는 [소요 시간, 요청 시각] 형태로 들어가서 소요 시간이 짧은 순으로 정렬됨
        while i < len(jobs) and start < jobs[i][0] <= current_time:
            heapq.heappush(hq, [jobs[i][1], jobs[i][0]])
            i += 1
            
        # 대기 큐(힙)에 작업이 있다면 수행
        if hq:
            duration, request_time = heapq.heappop(hq)
            start = current_time
            current_time += duration  # 작업이 끝난 시점으로 시간 이동
            total_turnaround_time += (current_time - request_time)  # 반환 시간 누적
        else:
            # 아직 들어온 작업이 없다면, 다음 작업의 요청 시각으로 현재 시간을 점프
            current_time = jobs[i][0]
            
    # 평균 반환 시간의 정수 부분 리턴
    return total_turnaround_time // len(jobs)