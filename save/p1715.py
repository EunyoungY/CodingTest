from queue import PriorityQueue
import sys
input = sys.stdin.readline
n = int(input())
que = PriorityQueue()

for _ in range(n):
    que.put(int(input()))

sum = 0
for i in range(n-1):
    temp = que.get()
    temp += que.get()
    sum += temp
    que.put(temp)
    # print(i, que.queue)


print(sum)

'''
3
10
20
40
'''
