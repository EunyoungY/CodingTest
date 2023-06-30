# 1 2 2 2 3
# [1,1][2,3][3,1]
# 2
n = int(input())
dic = {}
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
for num in N:
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

dic = sorted(dic.items())


def bin_search(target):
    find = 0
    start = 0
    end = len(dic)-1
    while start <= end:
        mid = (start+end)//2
        if dic[mid][0] < target:
            start = mid+1
        elif dic[mid][0] > target:
            end = mid-1
        else:
            find = dic[mid][1]
            break
    return find


answer = []
for target in M:
    answer.append(bin_search(target))

print(*answer)
