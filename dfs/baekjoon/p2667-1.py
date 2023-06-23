import sys
from collections import deque
# input = sys.stdin.readline #TODO
n = int(input())
arr = [] 
for _ in range(n):
    # arr.append(list(input().rstrip()))  # TODO
    arr.append(list(map(int, input())))  # TODO

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    q = deque()
    q.append([a, b])
    arr[a][b] = 0
    depth = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] = 0
                depth += 1
    return depth

answers = []
for i in range(n):
    for j in range(n): 
        if arr[i][j] == 1: 
            answers.append(bfs(i,j)) 

answers.sort()
print(len(answers))
for answer in answers:
    print(answer)

'''
n*n반복
bfs끝날 때마다 answer +=1
output:첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
'''
