import sys

n, k = map(int, input().split())
kids = list(map(int, input().split()))

diff=[]
for i in range(1, n):
    diff.append(kids[i]-kids[i-1])

diff.sort() 
print(sum(diff[:n-k]))