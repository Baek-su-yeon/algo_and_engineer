def solution(sizes):
    max_row = 0
    max_col = 0
    
    for row, col in sizes:
        if row < col:
            row, col = col, row
        
        max_row = max(max_row, row)
        max_col = max(max_col, col)
    
    return max_row * max_col

# 한줄 풀이
def solution(sizes):    
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)