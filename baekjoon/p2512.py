n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start, end = 0, max(arr)
budget, ans = 0, 0
if sum(arr) <= m:
    print(max(arr))
    exit()
while start <= end:
    money = 0
    mid = (start+end)//2
    print('*', start, mid, end)
    for num in arr:
        money += min(num, mid)
    if money <= m:
        start = mid+1
    else:
        end = mid-1
    print(' ', start, mid, end)
print(end)
