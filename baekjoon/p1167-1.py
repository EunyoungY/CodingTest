n = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(n):
    row = list(map(int, input().split()))
    for i in range(1, len(row)-2, 2):
        arr[row[0]].append((row[i], row[i+1]))


def dfs(v, depth):
    global distances
    distances[v] = max(distances[v], depth)
    for node, weight in arr[v]:
        if distances[node] == -1:
            dfs(node, depth+weight)


distances = [-1]*(n+1)
dfs(1, 0)
start = distances.index(max(distances))
distances = [-1]*(n+1)
dfs(start, 0)
print(max(distances))
# n = int(input())
# arr=[[] for _ in range(n+1)]
# visited=[False]*(n+1)

# for _ in range(n):
#     row = list(map(int,input().split()))
#     for i in range(1, len(row)-2, 2):
#         arr[row[0]].append((row[i], row[i+1]))

# distances = [0]*(n+1)
# def dfs(v, depth):
#     global distances
#     visited[v] = True
#     distances[v] = max(distances[v], depth)
#     for node, weight in arr[v]:
#         if not visited[node]:
#                 dfs(node, depth+weight)
#     visited[v] = False

# dfs(1,0)
# start = distances.index(max(distances))
# distances=[0]*(n+1)
# dfs(start, 0)
# print(max(distances))
