n, m = map(int, input().split())
arr = sorted(map(int, input().split()))


def bt(depth, lst):
    if depth == m:
        print(*lst)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            bt(depth+1, lst+[arr[i]])
            visited[i] = False


visited = [False] * n
bt(0, [])
