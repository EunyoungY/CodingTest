n, m = map(int, input().split())

def bt(depth, lst):
    if depth == m:
        print(*lst)
        return
    for i in range(1, n+1):
        if len(lst) ==0 or lst[-1] <= i:
            bt(depth+1, lst+[i])  
bt(0, [])