import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m, v = map(int, input().split())
A = [[]for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)


def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in sorted(A[v]):
        if not visited[i]:
            DFS(i)
 
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        print(now_node, end=' ')
        for i in sorted(A[now_node]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)

DFS(v)

print()
visited = [False]*(n+1)

BFS(v)


'''
1000 1 1000
999 1000

4 5 1
1 2
1 3
1 4
2 4
3 4
'''
