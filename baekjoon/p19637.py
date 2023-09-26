import sys
input = sys.stdin.readline
n, m = map(int, input().split())
level = []
arr = []
for _ in range(n):
    chingho, num = input().split()
    level.append((chingho, int(num)))

for _ in range(m):
    arr.append(int(input()))

for num in arr:
    start, end = 0, n-1
    while start <= end:
        mid = (start+end)//2 
        if num <= level[mid][1]:
            end = mid-1
        else:
            start = mid+1 
    print(level[start][0])
