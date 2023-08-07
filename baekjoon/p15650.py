n, m = map(int, input().split())

def bt(depth, start, lst):
    if depth == m:
        print(*lst)
        return
    for i in range(start, n+1):
        bt(depth+1, i+1, lst+[i])
    
bt(0, 1, [])