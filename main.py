
def proc1():
    N = 5
    chars = []
    for i in range(N):
        chars.append(input())
    line = ' '.join(chars)
    print(line)

def proc2():
    line = []
    while True:
        line.append(input('Введите слова или слово stop : '))
        if 'stop' in line:
            break
    print(' '.join(line)[:-4])

def proc3():
    word = str(input('Введите слово: '))
    for i in range(len(word)):
        if word[i] != "Ф" or word[i] != "ф":
            flag = True
        else:
            flag = False
    if flag:
        print('Это редкое слово!!')
    else:
        print('Это не редкое слов:(')

def proc4():
    import random
    cnt = 0
    cntt = 0
    while cntt < 3:
        numb1 = random.randint(1, 5)
        numb2 = random.randint(1, 5)
        ans = numb1 + numb2
        print(numb1, '+', numb2, '=')
        if ans == int(input()):
            print('Правильный ответ!')
            cnt += 1
        else:
            print('Ответ неверный!')
            cntt += 1
    else:
        print('Игра окончена. Правильных ответовв:', cnt)


proc1(), proc2(), proc3(), proc4()