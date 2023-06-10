from collections import deque
n = int(input())

result = deque()
for i in range(1, n+1):
    result.append(n-i+1)

for i in range(n):
    if len(result) > 1:
        result.pop()
        bottom = result.pop()
        result.appendleft(bottom)
print(result[0])
