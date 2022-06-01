stopper = 0
while stopper != 1:

    score = 0

    answer = input('Год рождения Максима Галкина: ')
    #1976
    if answer == '1976':
        score = score + 1
    else:
        score = score

    answer = input('Год рождения Аллы Пугачёвой: ')
    #1949
    if answer == '1949':
        score = score + 1
    else:
        score = score

    answer = input('Год рождения Филиппа Киркорова: ')
    #1967
    if answer == '1967':
        score = score + 1
    else:
        score = score

    answer = input('Год рождения Сергея Зверева: ')
    #1963
    if answer == '1963':
        score = score + 1
    else:
        score = score

    answer = input('Год рождения Бориса Моисеева: ')
    #1954
    if answer == '1954':
       score = score + 1
    else:
        score = score

    wrongs = 5 - score
    correctpercent = score * 100 / 5
    wrongpercent = 100 - correctpercent

    print('Количество правильных ответов:', score)
    print('Количество неправильных ответов:', wrongs)
    print('Процент правильных ответов:', correctpercent)
    print('Процент неправильных ответов:', wrongpercent)

    proceed = input('Вы хотите начать игру сначала? (да/нет): ')
    if proceed == 'нет':
        break