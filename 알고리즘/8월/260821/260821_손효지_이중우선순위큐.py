def solution(operations):
    q = []
    
    for op in operations:
        command, val = op.split()
        val = int(val)
        
        if command == 'I':
            # 숫자를 큐에 삽입
            q.append(val)
        elif command == 'D':
            if not q:
                continue # 큐가 비어있으면 연산 무시
            
            if val == 1:
                # 최댓값 삭제: 정렬 후 가장 큰 값(마지막 요소) 제거
                q.sort()
                q.pop()
            elif val == -1:
                # 최솟값 삭제: 정렬 후 가장 작은 값(첫 번째 요소) 제거
                q.sort()
                q.pop(0)
                
    # 최종 결과 반환
    if not q:
        return [0, 0]
    else:
        return [max(q), min(q)]