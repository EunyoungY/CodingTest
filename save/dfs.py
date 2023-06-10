import sys
sys.setrecursionlimit(10000)


def dfs(depth):
    if depth == 3:
        return
    print(depth, 'before')
    dfs(depth+1)
    # dfs(depth+1)
    print(depth, 'after')


dfs(0)
