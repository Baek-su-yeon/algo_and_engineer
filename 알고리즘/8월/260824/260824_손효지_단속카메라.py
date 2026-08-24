def solution(routes):

    
    # 첫 값 기준 순서대로 정렬해보기
    routes.sort(key=lambda x: x[1])

    camera = -30001 # 첫 카메라 위치 (문제 범위보다 작은 값임)
    answer = 0
    
    for route in routes:
        start, end = route
        
        # 현 위치가 이 차량의 진입 시점보다 앞에 있다면(단속X)
        if camera < start:
            answer += 1
            camera = end   # 차량이 나가는 지점에 새로운 카메라 설치
    
    return answer