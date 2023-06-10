# selection sort
# a = list(input())

# max = 0
# for i in range(len(a)-1):
#     max = i
#     for j in range(i, len(a)):
#         if a[j] > a[max]:
#             max = j
#     if a[i] < a[max]:
#         temp = a[i]
#         a[i] = a[max]
#         a[max] = temp

# print(*a, sep='')

import sys
a = list(sys.stdin.readline())
print(*sorted(a, reverse=True), sep='')

'''
2143
61423
500613009
'''
