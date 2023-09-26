n, k, d = map(int, input().split())
arr = [0]*(n+1)
cnt = 0
for _ in range(k): 
    s, e, j = map(int, input().split())
    for i in range(s, e+1, j):
        arr[i] += 1
        cnt += 1

start, end = 1, n
while start <= end:
    mid = (start+end)//2
    if sum(arr[start:mid+1])<d:
        end += end-mid 
    elif sum(arr[start:mid+1])>=d:
        end = mid-1 
print(end)
 
# print(arr)
