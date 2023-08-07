n = int(input())

answer = 0
x = n//5

for i in range(x, -1, -1):
    # print(i,(n-5*i)%3 )
    if (n-5*i) % 3 == 0:
        answer = i + (n-5*i)//3
        print(answer)
        exit()
print(-1)
