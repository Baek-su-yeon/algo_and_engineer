def DFS(n, nodes):
    visited = [False] * (n + 1)
    stack = []

    stack.append(1)

    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True

            for next in nodes[now]:
                stack.append(next)

    return abs((n - sum(visited)) - sum(visited))


def solution(n, wires):
    answer = 100

    for i in range(len(wires)):
        nodes = [[] for _ in range(n + 1)]

        for j in range(len(wires)):

            if i == j: continue

            left = wires[j][0]
            right = wires[j][1]

            nodes[left].append(right)
            nodes[right].append(left)

        diff = DFS(n, nodes)

        answer = min(answer, diff)


    return answer