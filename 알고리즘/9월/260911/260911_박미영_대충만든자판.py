# 휴대폰 자판에는 하나의 키에 여러 개의 문자가 할당될 수 있음.
# 키 하나에 여러 문자가 할당된 경우, 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀜.
# 휴대폰 자판은 키의 개수가 1~100개까지 있을 수 있음.
# 특정 키를 눌렀을 때, 입력되는 문자들도 무작위로 배열
# 같은 문자가 자판 전체에 여러 번 할당된 경우도 있음.
# 키 하나에 같은 문자가 여러 번 할당된 경우도 있음.
# 아예 할당되지 않은 경우도 존재
# 이 휴대폰 자판으로 특정 문자열을 작성할 때, 키를 최소 몇 번 눌러야 그 문자열을 작성할 수 있는가
# keymap : 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열 배열
# targets : 입력하려는 문자열들이 담긴 문자열 배열 
# 목표 문자열을 작성할 수 없을 때는 -1 저장 

def solution(keymap, targets):
    count = {} # 문자열 몇 번 눌러야되는지
    
    for k in keymap:
        for i in range(len(k)):
            if k[i] in count:
                count[k[i]] = min(count[k[i]], i+1)
            else:
                count[k[i]] = i+1
                
    answer = []
    for target in targets:
        target_count = 0
        for t in target:
            if t not in count:
                target_count = -1
                break
                
            target_count += count[t]
            
        answer.append(target_count)
        
    return answer
