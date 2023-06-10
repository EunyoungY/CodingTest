import math
n = int(input())


def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def DFS(v):
    for i in range(5):
        if isPrime(v) == True:
            if len(str(v)) == n:
                print(v)
                return
            else:
                DFS(v*10 + 2*i+1)


DFS(2)
DFS(3)
DFS(5)
DFS(7)
