from dataclasses import field

um = 0
while True:

    num += 1

    show()

    if num % 2 == 1:
        print('Ходит крестик:')
    else:
        print('Ходит нолик:')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'Y'

    if num == 9:
        print('Ничья!')
        break

#print(num)
for i in range(3):
        if field()[i][0] == field()[i][1] == field()[i][2] != " ":
            return field()[i][0]  # Вернуть символ победителя
        if field()[0][i] == field()[1][i] == field()[2][i] != " ":
            return field()[0][i]

    # Проверка диагоналей
    if field()[0][0] == field()[1][1] == field()[2][2] != " ":
        return field()[0][0]
    if field()[0][2] == field()[1][1] == field()[2][0] != " ":
        return field()[0][2]