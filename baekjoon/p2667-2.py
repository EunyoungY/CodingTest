from collections import deque
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0


def dfs(x, y):
    global cnt
    arr[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
            dfs(nx, ny)


def bfs(a, b):
    global cnt
    q = deque()
    q.append((a, b))
    arr[a][b] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0
                cnt+= 1


answers = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 0
            # dfs(i, j)
            bfs(i, j)
            answers.append(cnt)

print(len(answers))
answers.sort()
for a in answers:
    print(a)
