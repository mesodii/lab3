import random
cnt = 0
cntt = 0
while cntt < 3:
    numb1 = random.randint(1,5)
    numb2 = random.randint(1,5)
    ans = numb1 + numb2
    print(numb1, '+', numb2, '=')
    if ans == int(input()):
        print('Правильный ответ!')
        cnt += 1
    else:
        print('Ответ неверный!')
        cntt += 1
else:
    print('Игра окончена. Правильных ответовв:',cnt)

