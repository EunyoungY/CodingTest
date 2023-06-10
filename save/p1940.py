import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = list(map(int, input().split()))

i = 0
j = n-1
count = 0
arr.sort()
while(i < j):
    if arr[i]+arr[j] < m:
        i += 1
    elif arr[i]+arr[j] > m:
        j -= 1
    else:
        i += 1
        j -= 1
        count += 1
    print(i, j)
print(count)
