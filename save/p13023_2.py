import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
A = [[] for _ in range(n)]

visited = [0] * (n)

arrive = False


def dfs(now, depth):
    global arrive
    print(depth)
    if depth == 5:
        arrive = True
        return
    visited[now] = 1
    for i in A[now]:
        if visited[i] == 0:
            dfs(i, depth+1)
    visited[now] = 0


for i in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)


for i in range(n):
    visited = [0] * n
    dfs(i, 1)
    if arrive:
        break
if arrive:
    print('1')
else:
    print('0')
'''
5 4
0 1
1 2
2 3
3 4
=>1

'''
