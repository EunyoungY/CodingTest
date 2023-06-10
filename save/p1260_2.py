import sys
from collections import deque
sys.setrecursionlimit(10**6)
n, m, v = map(int, input().split())
A = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

for items in A:
    items.sort()
# print(A)


def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    q.append(v)
    visited[v] = True
    while q:
        curr = q.popleft()
        print(curr, end=' ')
        for i in A[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


visited = [False] * (n+1)
dfs(v)
print()

q = deque()
visited = [False] * (n+1)
bfs(v)

# print('hello', end=' ')
# print()
# print('world')
'''
4 5 1
2 4
1 2
3 4
1 3
1 4

'''
