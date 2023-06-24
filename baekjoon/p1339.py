import sys
n = int(input())

dic = {} # dic = [] #TODO
words = []
for i in range(n):
    word = input()
    words.append(word)
    for j in range(len(word)): 
        if word[j] not in dic:
            dic[word[j]] = 10**(len(word)-j-1)  
        else:
            dic[word[j]] += 10**(len(word)-j-1)

dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)

num = 9
answer = 0
for i in dic: 
    answer += i[1]*num
    num-=1 
print(answer)


'''
10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB
'''