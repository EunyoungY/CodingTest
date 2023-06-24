import heapq
n = int(input())
numbers =[]
for _ in range(n):
    heapq.heappush(numbers, int(input()))

answer = 0
while len(numbers)>1:
    a, b = heapq.heappop(numbers),heapq.heappop(numbers)
    answer += a+b
    heapq.heappush(numbers, a+b) 
print(answer)
