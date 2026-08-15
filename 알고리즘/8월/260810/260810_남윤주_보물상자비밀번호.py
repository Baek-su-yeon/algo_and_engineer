T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    s = input().strip()
    
    length = N // 4  
    numbers = set() 
    
    for _ in range(length):
        for i in range(0, N, length):
            password = s[i : i + length]
            numbers.add(password)
        
        # 회전
        s = s[-1] + s[:-1]
    
    result = [int(num, 16) for num in numbers]
    result.sort(reverse=True)
    
    print(f"#{tc} {result[K - 1]}")