coworkers = [ 'Chinara','Arina','Aija','Albina','Diana']
print(coworkers[0])
print(coworkers[4])
print(coworkers[::2])
print(coworkers[1::2])
print(len(coworkers))
new_coworkers = input('Введите имя:')
coworkers.append(new_coworkers)
print(coworkers)
print(len(coworkers))
coworkers_name = input ( 'Введите ваше имя:')
if coworkers_name in coworkers:
    print('Имя есть в списке')
else:
    print('Имени нет в списке')
