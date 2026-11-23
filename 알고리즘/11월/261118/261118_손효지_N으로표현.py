def solution(N, number):
    if N == number:
        return 1
        
    # 각 횟수별(1~8번)로 만들 수 있는 숫자를 저장할 리스트 (세트 활용)
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # 1. N을 i개 연속으로 이어 붙인 숫자 (예: 5, 55, 555)
        dp[i].add(int(str(N) * i))
        
        # 2. 사칙연산 조합 (j번 사용한 수와 i-j번 사용한 수의 조합)
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
                        
        # 3. 구하고자 하는 number가 현재 i번째 집합에 포함되어 있다면 즉시 i 반환
        if number in dp[i]:
            return i
            
    # 8번 초과인 경우 -1 반환
    return -1