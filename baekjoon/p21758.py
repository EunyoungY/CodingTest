n = int(input())
arr = list(map(int, input().split()))
ans = 0
arrLen = len(arr)
arrSum = sum(arr)

if arrLen == 3:
    print(max(arr)*2)
    exit()
# 벌 벌 벌통
for i in range(1, arrLen-1):
    ans = max(ans, sum(arr[1:])-arr[i] +sum(arr[i+1:])) 
    # print(1, i, ans, sum(arr[1:])-arr[i], sum(arr[i+1:]))

# 벌 벌통 벌
for i in range(1, arrLen):
    ans = max(ans, sum(arr[1:i])+sum(arr[i:-1]))
    # print(2, i, ans,  sum(arr[1:i]), sum(arr[i:-1]))
    
# 벌통 벌 벌
arr = list(reversed(arr))
for i in range(1, arrLen-1):
    ans = max(ans, sum(arr[1:])-arr[i] +sum(arr[i+1:])) 
    # print(3, i, ans, sum(arr[1:])-arr[i], sum(arr[i+1:]))

print(ans)

'''
7
9 9 4 1 4 9 9
'''