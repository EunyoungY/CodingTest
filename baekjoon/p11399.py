'''
N(1 ≤ N ≤ 1,000)

'''

# import sys
# n = int(input())
# row = list(map(int,input().split()))

# times = sorted(row)
# answers = times

# for i in range(1, n):
#     answers[i] += answers[i-1]
# print(sum(answers))  


import sys
n = int(input())
people = list(map(int,input().split()))

people.sort()
answer = 0
 
for i in range(n): 
    answer += sum(people[:i+1])
print(answer)  