n, m = map(int,input().split())

def bt(depth, lst):
    if depth == m:
        print(*lst)
        return
    for i in range(1,n+1):
        bt(depth+1, lst+[i])
bt(0,[])