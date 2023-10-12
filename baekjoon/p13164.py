n, k = map(int, input().split())
arr = list(map(int, input().split()))
subs=[]
for i in range(n-1):
    subs.append(arr[i+1]-arr[i])
subs.sort(reverse=True)
# print(subs)
print(sum(subs[k-1:]))