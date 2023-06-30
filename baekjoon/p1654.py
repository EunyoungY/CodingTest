k, m = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

def search():
    start = 1
    end = max(arr)
    while start<=end:
        cnt = 0    
        mid = (start+end)//2
        print(start, mid, end, end=' // ')
        for num in arr:
            cnt +=  num//mid
        if cnt < m:
            end = mid-1
        else : # cnt >= m
            start = mid+1
        print(cnt, start, mid, end)
    return end

print(search())