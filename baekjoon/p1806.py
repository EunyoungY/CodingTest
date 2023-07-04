import sys
n, s = map(int, input().split())
arr = list(map(int, input().split()))
sum_val = 0
answer = sys.maxsize
start, end = 0,0
while True:
    if sum_val >=s:
        answer = min(answer, end-start)
        sum_val -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        sum_val += arr[end]
        end += 1
if answer == sys.maxsize:
    print(0)
else:
    print(answer)
