
equation = input() 
A = equation.split('-')
len_A = len(A)
for i in range(len_A):
    b = A[i].split('+')
    sumV = 0
    for j in b:
        sumV += int(j)
    A[i] = sumV

len_A = len(A)
sumV = 0
for i in range(len_A):
    if i == 0:
        sumV += A[i]
    else:
        sumV -= A[i]

print(sumV)
'''
55-50+40
'''
