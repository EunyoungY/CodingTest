# 1-457
# 300 => cnt = + 802//30

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
start = 1
end = max(arr)
answer = 0
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for num in arr:
        cnt += num//mid
    if cnt >= n:
        # answer = max(answer, mid)
        start = mid+1
    if cnt<n:
        end = mid-1
print(end)