n, k = map(int, input().split())
kids = list(map(int,input().split()))

differences =[]
for i in range(n-1):
    differences.append(kids[i+1]-kids[i])

differences.sort()
print(sum(differences[:n-k]))