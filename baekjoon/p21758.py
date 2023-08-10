n = int(input())
arr = list(map(int, input().split()))
ans = 0
arrLen = len(arr)

toRight = [0]
toLeft = [0]
if arrLen == 3:
    print(max(arr)*2)
    exit()
for i in range(1, arrLen):
    toRight.append(toRight[i-1]+arr[i])

rArr = list(reversed(arr))
# print(rArr)
for i in range(1, arrLen):
    toLeft.append(toLeft[i-1]+rArr[i])
    
for i in range(1, arrLen):
    ans = max(ans, toRight[-1]-arr[i] + toRight[-1]-toRight[i], toLeft[-1]-arr[i] + toLeft[-1]-toLeft[i],)

print( ans) 
# print(list(reversed(toLeft)))