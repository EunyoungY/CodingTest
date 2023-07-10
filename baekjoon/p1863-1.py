n = int(input())
skyline = []
for _ in range(n):
    x, y = map(int, input().split())
    skyline.append(y)

stk = [0]
answer = 0
for p in skyline:
    height = p
    while stk[-1] > p:
        if stk[-1] != height:
            answer += 1
            height = stk[-1]
        stk.pop()
    stk.append(p)
print(answer)
