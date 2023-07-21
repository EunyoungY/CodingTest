import math
n = int(input())
primes=[2,3]
def get_prime(num):
    if num%2!=0 and num%3!=0:
        primes.append(num)
for i in range(2, n):
    get_prime(i)

answer  = 0
start, end = 0,0
summ = 0
while True:
    if summ==n:
        answer+=1
    if summ>n:
        summ-=primes[start] 
        start+=1
    elif end == len(primes):
        break
    else:
        summ+=primes[end]
        end+=1
    
print(answer)
