import sys
n = int(input())

# dic = [] #TODO
dic = {}
words = []
for i in range(n):
    word = input()
    words.append(word)
    for j in range(len(word)):
        if word[j] not in dic:
            # dic.update({word[j]: len(word)-(j+1)})
            dic[word[j]] = len(word)-(j+1)
        else:
            dic[word[j]] = max(dic[word[j]], len(word)-(j+1))

sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)  # TODO
print(sorted_dic)


dic = {}
for i in range(len(sorted_dic)):
    char, val = sorted_dic[i]
    dic[char] = 9-i
print(dic)

answer = 0
for word in words:
    for i in range(len(word)):
        answer += dic[word[i]]*(10**(len(word)-i-1))
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