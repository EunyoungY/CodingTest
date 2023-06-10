import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

result = 0

def DFS(v, depth):
    global result
    if depth == 5:
        result = 1
        return
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i, depth+1)
    visited[v] = False


for i in range(n+1):
    DFS(i, 1)
    if result == 1:
        break


print(result)
'''
8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7

5 5
0 1
1 2
2 3
3 0
1 4
'''
