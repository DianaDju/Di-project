numbers = {0,0,1,2,3,4,4,5,6,7,8,8,9}
new = int(input ('Введите число: '))
if new in numbers:
    numbers.remove(new)
    print(f'''Множество {numbers}. Длина множества {len(numbers)}''')
else:
    numbers.add(new)
    print(f'''Множество {numbers}. Длина множества {len(numbers)}''')

