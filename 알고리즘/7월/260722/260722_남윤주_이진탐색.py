T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    start_a, end_a = 1, P
    count_a = 0
    
    while start_a <= end_a:
        count_a += 1
        mid = (start_a + end_a) // 2
        
        if mid == Pa:
            break
        elif mid < Pa:
            start_a = mid
        else:
            end_a = mid

    start_b, end_b = 1, P
    count_b = 0
    
    while start_b <= end_b:
        count_b += 1
        mid = (start_b + end_b) // 2
        
        if mid == Pb:
            break
        elif mid < Pb:
            start_b = mid
        else:
            end_b = mid

    if count_a < count_b:
        print(f"#{tc} A")
    elif count_b < count_a:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")