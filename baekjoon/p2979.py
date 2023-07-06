a,b,c = map(int, input().split())
arr=[0]*101
for _ in range(3):
    i, j = map(int, input().split())
    for k in range(i,j):
        arr[k] +=1
answer = 0
for num in arr:
    if num == 1:
        answer+=a
    elif num == 2:
        answer+=2*b
    elif num==3:
        answer+=3*c
print(answer)