# plan 43mins
import sys
from collections import deque
import math
n = int(input())


arr = [[0]*n for _ in range(n)]
queen = 0
answer = 0

# dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
# dy = [1, 0, -1, 1, 0, -1, 1, 0, -1]

# print(math.ceil(7/2)) #Learned

dx = [-1, -1,1,1 ]
dy = [-1, 1,-1,1]
# implement 56mins


def put_queen(a, b):
    arr[a][b] = 3
    x, y = a, b
    for i in range(n):
        arr[x][i] = 3
        arr[i][y] = 3
    for j in range(4):
        for i in range(1, n):
            nx = x+dx[j]
            ny = y+dy[j]
            if 0 <= nx < n and 0 <= ny < n:
                arr[nx][ny] = 3
                x, y = nx, ny
        x, y = a, b

        # if 0<=nx2<n and 0<=ny2<n :
        #     arr[nx2][ny2] = 3
#    queen n개를 못 넣으면 return -1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            put_queen(i,j)
            print(i,j)
            answer+=1

def bfs(a,b):
    q = deque()
    q.append([a,b])
    # if arr[a][b] == 0 #바깥에서 처리
    arr[a][b] = 1
    queen+=1 #initialize
    # while q:
    #     x,y = q.popleft()
    #     for i in range(n):
            

#0; 놓을 수 있는 공간 
#3: 막힌 공간
#1: queen

# put_queen(0, 0)
# answer+=1
# put_queen(1, 2)
for i in range(n):
    print(arr[i])
print(answer)
'''
1) queen놓기(bfs 호출)
2) 8분면으로 queen 놓을 수 없는 공간 표시 : -1처리 
3) x(행)고정 y열(0-n)탐색하면서 queen 넣을 수 있는 경우 bfs에 모두 append
(x,y)순서쌍의 조합으로는 못하나? =? X
'''
