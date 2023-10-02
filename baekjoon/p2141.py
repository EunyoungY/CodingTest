import sys
input = sys.stdin.readline
n = int(input())
x, a = [], []
for _ in range(n):
    i, j = map(int, input().split())
    x.append(i)
    a.append(j)

f_sum = [a[0]]
b_sum = [sum(a)]
val = sys.maxsize
ans = 0
for i in range(0, n):
    print(f_sum[i], b_sum[i])
    if max(f_sum[i], b_sum[i]) < val:
        val = max(f_sum[i], b_sum[i])
        ans = x[i]
    # if i>0:
    #     print('f_sum',i, f_sum[i-1], a[i+1])
    f_sum.append(f_sum[i-1]+a[i])
    b_sum.append(b_sum[i]-f_sum[i-1])

print(ans)
'''
3
1 3
2 5
3 4 
'''
