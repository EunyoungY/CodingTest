p = int(input())

for _ in range(p):
    arr = list(map(int, input().split()))
    steps = 0
    for i in range(1,20):
        for j in range(i+1,21):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i] 
                steps +=1
    print(arr[0], steps)
                