'''
반드시 교환

가능한 가장 큰 금액
'''
def dfs(count):
    global max_val
    current_num = "".join(numbers)
    
    if (current_num, count) in visited:
        return
    visited.add((current_num, count))

    if count == change:
        max_val = max(max_val, int(current_num))
        return

    for i in range(length):
        for j in range(i + 1, length):
            numbers[i], numbers[j] = numbers[j], numbers[i]  
            dfs(count + 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]  
            
T = int(input())
for tc in range(1, T+1):
    numbers, change = input().split()
    numbers = list(numbers)
    length = len(numbers)
    change = int(change)
    max_val = 0
    visited = set()

    dfs(0)
    print(f'#{tc} {max_val}')