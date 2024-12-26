num = {'Nana':'0 555 20 06 01','Diku':'0 555 27 04 01','Ermek':'0 555 11 08 13','Adil':'0 555 21 05 16'}
print(f'Имена контактов: {num.keys()}')
print(f'Номера контактов: {num.values()}')
print('Контакты: ')
for key, value in num.items():
    print(f'{key} - {value}')
key = input('Введите новое имя контакта: ')
value = input('Введите номер телефона: ')
num[key] = value
print(f'Новый список контактов: {num}')
key = input('Введите новое имя контакта: ')
value = input('Введите номер телефона: ')
num[key] = value
print(f'Новый список контактов: {num}')
num['Diku'] = '0 555 27 01 04'
print(f'Обновленный список контактов: {num}')
friend = input('Введите имя контакта: ')
if friend in num.keys():
    print(f'Удаляем контакт: {friend} - {num[friend]}')
    del num[friend]
else:
    print(f'Номера нет в списке. ')
    new_num0 = input('Введите номер: ')
    num[friend] = 'new_num0'
    print(f'Новый список контактов: {num}')


