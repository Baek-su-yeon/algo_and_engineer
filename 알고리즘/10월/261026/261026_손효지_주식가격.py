def solution(prices):
    s = []
    time = [i for i in range(len(prices) - 1, -1, -1)]

    for i, price in enumerate(prices):
        while s and price < s[-1][0]:
            temp = s.pop()
            index = temp[1]
            time[index] = i - index

        s.append((price, i))

    return time