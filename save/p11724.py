# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline
# n, m = map(int, input().split())
# A = [[] for _ in range(n+1)]  # [[], [], []]
# visited = [False] * (n+1)


# def DFS(v):
#     visited[v] = True
#     for i in A[v]:
#         if not visited[i]:
#             DFS(i)


# for _ in range(m):
#     s, e = map(int, input().split())
#     A[s].append(e)
#     A[e].append(s)

# count = 0

# for i in range(1, n+1):
#     if not visited[i]:
#         count += 1
#         DFS(i)

# print(A)

'''
6 5
1 2
2 5
5 1
3 4
4 6
'''


# DFS
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    k, j = map(int, input().split())
    A[k].append(j)
    A[j].append(k)


def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


count = 0
for i in range(1, n+1):
    if visited[i] == False:
        count += 1
        DFS(i)

print(count)
