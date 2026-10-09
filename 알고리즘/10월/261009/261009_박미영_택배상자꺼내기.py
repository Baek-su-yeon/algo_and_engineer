# 왼쪽에서 오른쪽으로 가면서 1번부터 번호 순서대로 상자 한 개씩 놓기
# 가로에 w개 놓았다면 이번에는 오른쪽에서 왼쪽으로 가면서 그 위층에 택배 상자를 한 개씩 놓기
# 계속 반복하면서 n개의 상자를 모두 놓을 때까지 한 층에 w개씩 상자를 쌓음.
# 손님이 번호를 말하면 택배 상자를 꺼내주는데 A를 꺼내려면 A 위에 있는 모든 상자를 꺼내야 됨.
# 꺼내려는 상자 번호가 주어졌을 때, 꺼내려는 상자를 포함해 총 몇 개의 택배 상자를 꺼내야 하는가
# n : 창고에 있는 택배 상자의 개수
# w : 가로로 놓는 상자의 개수
# num : 꺼내려는 택배 상자의 번호
# 꺼내야 하는 상자의 총개수 출력

def solution(n, w, num):
    boxes = []
    
    even = 1
    for i in range(1, n+1, w):
        if even % 2 == 1:
            boxes.append(list(range(i, min(i+w, n+1))))
        else:
            boxes.append(list(range(min(i+w-1, n), i-1, -1)))
        even += 1
        
    row = (num - 1) // w + 1
    if row % 2 == 1:
        col = (num - 1) % w
    else:
        col = w - 1 - ((num - 1) % w)
        
    total_row = (n - 1) // w + 1
    answer = total_row - row + 1
    last = n % w

    if last != 0:
        top_row = total_row - 1

        if top_row % 2 == 0:
            if col >= last:
                answer -= 1
        else:
            if col < w - last:
                answer -= 1

    return answer
    
