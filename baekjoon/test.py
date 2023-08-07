import math
a, b = 10, 100

def is_prime(num):    
    state = True
    # print(int(math.sqrt(num))+1)
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return state

primes=[]
for i in range(10, 100):
    if is_prime(i)==True:
        primes.append(i)

# print(is_prime(11))
print(primes)
print(len(primes))