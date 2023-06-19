'''
(1 ≤ N ≤ 100,000) 
'''

import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

answer = 0
while len(cards) > 1:
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, temp)
    answer += temp

print(answer)

# 시간초과!!!!!
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr =[]
# for i in range(n):
#     arr.append(int(input()))

# arr.sort()

# ans = 0
# for i in range(n):
#     ans += sum(arr[:i+1])
# print(ans-arr[0])
