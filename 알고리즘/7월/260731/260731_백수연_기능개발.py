def solution(progresses, speeds):
    answer = []
    
    while progresses:
        
        # 하루 작업
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        # 배포 확인
        count = 0
        for _ in range(len(progresses)):
            if 100 <= progresses[0]:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
                
            else:
                break
        
        if 0 < count: answer.append(count)
    
    return answer