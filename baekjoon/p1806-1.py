import sys
input = sys.stdin.readline
 
 
N, S = map(int, input().split())
arr = list(map(int, input().split()))
 
result = N+1
_sum = 0
left = 0
right = 0
while True:
    if _sum >= S:
        result = min(result, right-left)
        _sum -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        _sum += arr[right]
        right += 1
 
if result == N+1:
    print(0)
else:
    print(result)