n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

N.sort()
 
def bin_search(target):
    find = 0
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2 
        if N[mid] < target:
            start = mid+1
        elif N[mid] > target:
            end = mid-1
        else:
            find = 1
            break 
    print(find)

for num in M:
    bin_search(num)
