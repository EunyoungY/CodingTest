n = int(input())
dic = {}
for _ in range(n):
    row = list(input())
    for i in range(len(row)):
        if row[i] not in dic:
            dic[row[i]] = 10**(len(row)-i-1)
        else:
            dic[row[i]] += 10**(len(row)-i-1)

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True) 

answer =0
for i in range(len(dic)):
    answer += dic[i][1]*(9-i) 
    
print(answer)
    