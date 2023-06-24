'''
Plan: 13 mins
algorithm: dfs/bfs
time complexity: O(N+E)

n input
list input

def bfs

bfs()
//1로 구성된 연결이 끊긴걸 어떻게 알고 각 단지를 어떻게 count하지?
- n,n에 도착할때까지 
- depth를 세기
- 탐색이 끝난 위치에서 bfs()다시 시작하기: 종료조건, 1이 없을 때까지? or n,n에 도착할 때까지?
- Visited 따로 안하고 1표시를 0으로 바꾸면서 방문 기록
//0으로 연결된 곳은 어떻게 지나가지?
'''
# implementaion : 65mins -> fail
'''
hint
1. 시작점을 모르기 때문에 1인 지점을 찾아 탐색을 시작
2. 이미 방문한 곳은 0으로 바꿔주기

Plan2 & Implement: 10 + 30 mins
main에서 x,y에 대해 반복문을 돌아 arr[x][y] =1인 시작점 찾아서 dfs실행

Trial n: 답 틀린 이유
Sort를 안함: 문제에서 오름차순으로 정렬하라고 했는데, 예제 풀었을 때 이미 정렬된 채로 나와서 생각 못함
'''
import sys
from collections import deque
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []

q = deque()


def bfs(a, b):
    # depth = 0
    q.append([a, b]) 
    arr[a][b] = 0 # MISS
    depth = 1 # Mistake: depth = 0
    while q:
        x,y = q.popleft()  #쉽게 빼는 팁
        # curr = q.popleft()
        # x = curr[0]
        # y = curr[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1:
                    # q.append(arr[nx][ny]) # Mistake
                    q.append([nx, ny])
                    arr[nx][ny] = 0
                    depth += 1
    answer.append(depth)

print(arr)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i, j)

print(len(answer))
answer.sort()
for i in answer:
    print(i)
