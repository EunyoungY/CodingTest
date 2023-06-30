n, m = map(int, input().split())
trees = list(map(int,input().split()))

def search():
    answer = 0
    start = 0
    end = max(trees)
    while start<=end: 
        mid = (start+end)//2
        for tree in trees:
            answer += tree-mid
        if answer >= m:
            start = mid+1
        else:
            end = mid-1
    return answer

print(search())