import sys
input = sys.stdin.readline
n, c = map(int, input().split())
arr = [int(input().rstrip()) for _ in range(n)]
arr.sort()
start, end = 1, arr[-1]-arr[0]
ans = 0

 
while start <= end:
    mid = (start+end)//2
    cnt = 1
    location = arr[0]
    for i in range(1, n):
        if arr[i]-location >= mid:
            cnt += 1
            location = arr[i]
    if cnt < c:
        end = mid-1
    else:
        start = mid+1
        ans = mid
print(ans)
