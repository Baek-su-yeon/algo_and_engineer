def solution(nums):
    answer = 0
    mon = {}
    for num in nums:
        if num not in mon:
            mon[num] = 1
        else:
            mon[num] += 1
    
    con = len(nums) // 2
    if len(mon) >= con:
        answer = con
    else:
        answer = len(mon)
    return answer
