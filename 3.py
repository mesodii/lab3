word =str(input('Введите слово: '))
for i in range(len(word)):
    if word[i] != "Ф" or word[i] != "ф":
       flag = True
    else:
        flag = False
if flag:
    print('Это редкое слово!!')
else:
    print('Это не редкое слов:(')