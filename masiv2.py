n = int(input('Введите количество дел: '))
todo = []
print('Запишите свои дела: ')
for i in range(n):
    task = (input('Введите дело: '))
    todo.append(task)
    print(todo)
print('Измените задачу на сегодня: ')
index = todo.index(input('Введите название дела: '))
print(f'{index} - Индекс вашего задания')
todo[index] = input('Введите новое задание: ')
print(f'Новый список задач: {todo}')
print('Удалите ненужное дело: ')
index2 = todo.index(input('Введите название дела, которое хотите удалить: '))
task1 = todo.pop(index2)
print(f'Удаленное дело: {task1}')
print(f'Новый список задач: {todo}')