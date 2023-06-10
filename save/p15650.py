import sys
# n, m = map(int, input().split())

# answer = []
# visited = [False] * (n+1)

# result = []
# def dfs(depth):
#     if depth == m:
#         print(result)
#         # print(' '. join(map(str, result)))
#         return
#     for i in range(1, n+1):
#         if not visited[i]:
#             visited[i] = True
#             result.append(i)
#             dfs(depth+1)
#             visited[i] = False
#             result.pop()
# dfs(0)
 
n, m = list(map(int, input().split()))
s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()


dfs(1)
'''
4 2  
'''
