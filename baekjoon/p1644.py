n = int(input())

# prime_num = [2, 3]

# for i in range(4, n+1):
#     if i % 2 != 0 and i % 3 != 0:
#         prime_num.append(i)
a = [False, False] + [True] * (n-1)
prime_num = []

for i in range(2, n+1):
    if a[i]:
        prime_num.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

# left, right = 0, 0
# count = 0
# while right<=len(prime_num):
#     summ = sum(prime_num[left: right])
#     if summ == n:
#         count += 1
#         right+=1
#     elif summ < n:
#         right += 1
#     else:
#         left += 1
# print(count)

# 2 3
# n = 3
start, end = 0, 0
count = 0
summ = 0
while True:
    if summ == n:
        count += 1
    if summ > n:
        summ -= prime_num[start]
        start += 1
    elif end == len(prime_num):
        break
    else:
        summ += prime_num[end]
        end += 1

print(count)
