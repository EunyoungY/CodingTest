n, m = map(int, input().split())
tmp = sorted(map(int, input().split()))
arr = []
for a in tmp:
    if a not in arr:
        arr.append(a)


def bt(depth, lst):
    if depth == m:
        print(*lst)
        return
    for a in arr:
        if not lst or lst[-1] <= a:
            bt(depth+1, lst+[a])


bt(0, [])
