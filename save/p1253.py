import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

i = 0
j = N-2
k = N-1
count = 0
arr.sort()

while i < j:
    print(i, j, k)
    if arr[i]+arr[j] == arr[k]:
        count += 1
    j -= 1
    k -= 1

print(count)
