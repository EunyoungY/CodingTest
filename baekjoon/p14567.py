import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph=[1]*(n+1)
arr=[]
for _ in range(m):
    a, b = map(int, input().split())
    arr.append((a,b))
arr.sort()

for a, b in arr:  
    graph[b] = max(graph[a]+1, graph[b]) 

print(*graph[1:])