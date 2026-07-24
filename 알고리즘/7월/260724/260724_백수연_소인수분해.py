def solution(n):
    answer = []
    check = [False] * 10001
    
    divisor = 2
    
    while n != 1:
        
        if n % divisor == 0:
            
            n /= divisor
            
            if not check[divisor]:
                check[divisor] = True
                answer.append(divisor)
            
        else: divisor += 1
        
        
    return answer