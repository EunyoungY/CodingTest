from queue import PriorityQueue
import sys
input = sys.stdin.readline
n = int(input())
q = PriorityQueue()

for _ in range(n):
    q.put(int(input()))

sum = 0
while q.empty() == False:
    if q.qsize() == 1:
        sum += q.queue[0]
        break
    else:
        a = q.get()
        b = q.get()
        if a < 0 and b <= 0:
            sum += max(a*b, a+b)
        elif a >= 0 and b >= 0 or a < 0 and b > 0:
            if q.qsize() % 2 == 0:
                sum += max(a*b, a+b)
            else:
                sum += a
                q.put(b)


print(sum)

# 조건문을 나눌 때   -, 0, + 의  조합(6개)을 나열하고 코딩했으면 시간을 아낄 수  있었을 것

'''
4
-1
2
1
3
'''
