n, m = map(int, input().split())


def bt(depth, lst):
    if depth == m:
        print(* lst)
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            bt(depth+1, lst+[i])
            visited[i] = False

visited = [False] * (n+1)
bt(0, [])
