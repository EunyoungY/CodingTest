#[구현 10Mins]
import sys
n, m = map(int, input().split())
arr = [[] for _ in range(n)]
visited = [False] * n
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

output = 0
print(arr)
def dfs(v, depth):
    global output
    visited[v] = True
    print(f'dfs({v}, {depth})', visited)
    if depth == 5:
        output = 1
        return
    for i in arr[v]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[v] = False #NEED

for i in range(n):
    if output == 0:
        dfs(i, 1)
        # visited = [False] * n #REMOVE

if output == 0:
    print(0)
else:
    print(1)
    
# def dfs1(v, depth):
#     global output
#     visited[v] = True
#     if depth == 5:
#         output = 1
#         return
#     for i in arr[v]:
#         if not visited[i]:
#             visited[i] = True  # NEED
#             dfs(i, depth+1)
#             visited[i] = False  # NEED
# for i in range(n):
#     if output == 0:
#         dfs1(i, 1)
#         visited = [False] * n 



'''
[12 mins]
유형: dfs
n,m 입력
arr = [[]*n]
visited = [False]*n
for _ in range m:
    arr에 저장

output = 0
def dfs(v)
    visited
    if depth == 5:
        output = 1
        return
    dfs

시작점에 따라 depth가 달라지니 각 vertex를 시작점으로 두고 dfs수행을 반복해야함
for i in range(n):
    dfs(i)
    visited = [False]*n

결과값
A,B,C,D,E가 존재: 1
아니면 0

=> Depth >= 5: 1 
'''