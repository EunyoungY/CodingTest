arr = [list(map(int, input().split())) for _ in range(19)]

dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]


def check(x, y):
    for i in range(4):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < 19 and 0 <= ny < 19 and arr[x][y] == arr[nx][ny]:
            cnt += 1
            nx+=dx[i]
            ny+=dy[i]
            if cnt == 5:
                if not (0 <= nx < 19 and 0 <= ny < 19 and arr[x][y] == arr[nx][ny]):
                    if not(0 <= x-dx[i] < 19 and 0 <= y-dy[i] < 19 and arr[x][y] == arr[x-dx[i]][y-dy[i]]):
                        print(arr[x][y])
                        print(x+1, y+1)
                        exit()
                else:
                    break


for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            check(i, j)

print(0)
