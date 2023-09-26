# n, m = map(int, input().split())
# apples = int(input())
# arr = [0] + [int(input()) for _ in range(apples)]
# ans = 0
# dis = 0
# start = 1
# for apple in arr:
#     if start <= apple <= start+m-1:
#         pass
#     elif start > apple:
#         ans += abs(start-apple)
#         start = apple
#     else:
#         ans += apple - (start+m-1)
#         start = apple - (m-1)

#     # if start < end:
#     #     dis += end - (start+m-1)
#     # elif start > end:
#     #     dis += start-(m-1) - end

# print(ans)

import sys
N, M = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())
now = 1
apples = []
answer = 0
for _ in range(J):
    apples.append(int(sys.stdin.readline()))
for apple in apples:
    if now <= apple <= now + (M-1):
        continue
    elif now > apple:
        answer += now-apple
        now = apple
    else:
        answer += apple - (M-1) - now
        now = apple - (M-1)
print(answer)