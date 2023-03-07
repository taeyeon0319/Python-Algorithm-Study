# 게임 개발

n, m = map(int, input().split())

x, y, pos = map(int, input().split())

graph = [] * n
direction = [0, 1, 2, 3]
go = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [[False] * m for _ in range(n)]
visited[x][y] = True

for i in range(n):
    graph.append(list(map(int, input().split())))


def turn_left(curr):
    if curr == 0:
        return 3
    return curr - 1


turn = 0
answer = 1

while 1:

    pos = turn_left(pos)
    dx = x + go[pos][0]
    dy = y + go[pos][1]

    if graph[dx][dy] == 0 and visited[dx][dy] == False:
        answer += 1
        visited[dx][dy] = True
        x, y = dx, dy
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:
        dx = x - go[pos][0]
        dy = y - go[pos][0]

        if graph[dx][dy] == 0:
            x, y = dx, dy
        else:
            break
        turn = 0
print(answer)
