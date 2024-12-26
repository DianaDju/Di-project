field = [[" - "]*3 for i in range(3)] # Создаем пустой двумерный массив
#print(field)

def show():
    ''' Функция преобразует поле в красивый вид '''
    print('  |  0  |  1  |  2  |')
    print('  ------------------ ')
    for i in range(len(field)):
        print(f'{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |')
        print('  ------------------ ')
#show()

def ask(f):
    while True:
        cords = input('  Введите координаты: ').split()

        if len(cords) != 2:
            print(' Введите 2 координаты!')
            continue

        x, y = cords

        if not(x.isdigit() and (y.isdigit())):
            print(' Ведите числа! ')
            continue

        x, y = map(int,cords)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты все диапазона!')
            continue

        if f[x][y] != " - ":
            print(' Клетка занята!')
            continue

    return x, y
ask(field)

