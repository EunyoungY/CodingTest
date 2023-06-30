n, m = map(int, input().split())
trees = list(map(int, input().split()))


def search():
    start = 1
    end = max(trees)
    while start <= end:
        answer = 0
        mid = (start+end)//2
        for tree in trees:
            answer += max(tree-mid,0)
        if answer >= m:
            start = mid+1
        else:
            end = mid-1
    return end


print(search())
