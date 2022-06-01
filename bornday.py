birthyear = input('Назовите год рожедения А.С. Пушкина: ')

if birthyear == ('1799'):
    print('Верно')
    birthdate = input('Назовите день рождения А.С. Пушкина: ')
    if birthdate == ('26.05.') or birthdate == ('26.05'):
        print('Поздравляю, вы сдали ЕГЭ!')

    else:
        print('Неверная дата')
        print('Вы не сдали ЕГЭ')


else:
    print('Неверный  год')
    print('Вы не сдали ЕГЭ')
