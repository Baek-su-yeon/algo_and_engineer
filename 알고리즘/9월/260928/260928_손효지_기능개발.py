import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    cnt = 0     
    max_day = days[0]  # 기준일
    
    for d in days:
        if d <= max_day:
            cnt += 1
        else:
            answer.append(cnt)
            max_day = d
            cnt = 1

    answer.append(cnt)
                        
    return answer