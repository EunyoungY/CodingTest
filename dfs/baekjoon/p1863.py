import sys
input = sys.stdin.readline
n = int(input())

heights = []
answer = 0
for i in range(n):
    x, y = map(int, input().split()) 
    if y == 0 :
        answer += len(set(heights))
        heights = []
    else:
        heights.append(y)
answer += len(set(heights))
print(answer)
