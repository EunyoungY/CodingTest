# from collections import deque

# n = int(input())
# arr = [[] for _ in range(n+1)]

# for i in range(1, n+1):
#     row = list(map(int, input().split()))
#     for j in range(1, len(row)-2, 2): 
#         arr[i].append((row[j], row[j+1]))
  
# def bfs(i):
#     dis = [0]*(n+1)
#     visited = [False]*(n+1)
#     q = deque()
#     q.append(arr[i][0])
#     visited[i] = True 

#     while q:
#         v, d = q.popleft()
#         for a in arr[v]:
#             if not visited[a[0]]:
#                 visited[a[0]] = True
#                 q.append(a)
#                 dis[a[0]] = dis[v] + a[1]

#     return dis
# print(bfs(1))

 
 
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
visited = [False]*(n+1)
arr = [ [] for _ in range(n+1) ]

for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, len(row)-2, 2): 
        arr[i].append((row[j], row[j+1]))

distance = [0] * (n+1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start]=True
    while len(queue)!=0:
        node = queue.popleft()
        for i in arr[node]:
            if visited[i[0]] == False:
                queue.append(i[0])
                visited[i[0]]=True
                distance[i[0]]= distance[node]+i[1]

bfs(1)
print(distance)
result_index = distance.index( max(distance) )
visited = [False]*(n+1)
distance = [0] * (n+1)
bfs(result_index)
print(max(distance))