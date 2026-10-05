# 현재 체력이 최대 체력보다 커지는 것은 불가능
# 기술을 쓰는 도중 공격을 당하면 기술이 취소되고, 공격을 당하는 순간에는 체력 회복 X
# 공격당해 기술이 취소당하거나 기술이 끝나면 그 즉시 '붕대 감기'를 다시 사용하며, 연속 성공 시간이 0으로 초기화
# 공격을 받으면 피해량만큼 현재 체력이 줄어듦.
# 체력이 0 이하가 되면 더 이상 체력 회복 X
# bandage : [시전 시간, 초당 회복량, 추가 회복량]
# health : 최대 체력
# attacks[i] : [공격 시간, 피해량] 형태의 길이가 2인 정수 배열  
# 공격이 끝난 직후 남은 체력 출력
# 체력이 0 이하가 되어 죽는다면 -1 출력

def solution(bandage, health, attacks):
    t = bandage[0] # t초 동안 붕대를 감음.
    x = bandage[1] # 1초마다 x만큼의 체력 회복
    y = bandage[2] # t초 연속으로 붕대를 감으면 y만큼의 체력 추가로 회복 
    
    cur = 0 # 현재 시간
    i = 0 # 몇 번째 공격
    r = 0 # 회복하는 시간 
    cur_health = health # 현재 체력
    
    while i < len(attacks):
        r = attacks[i][0] - cur - 1
        recovery_health = r * x
        plus_health = (r // t) * y
        cur_health = min(health, cur_health + recovery_health + plus_health)
        
        cur_health -= attacks[i][1]
        
        if cur_health <= 0:
            return -1
        else:
            cur = attacks[i][0]
            i += 1
    
    return cur_health
        
