line = []
while True:
    line.append(input('Введите слова или слово stop : '))
    if 'stop' in line:
        break
print(' '.join(line)[:-4])





