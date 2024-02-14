
my_list = ['1']
'''Удаляет из списка все имеющиеся в нём значения.'''
my_list.clear()
print(my_list)

my_list.append('hfrth')
print(my_list)



del my_list[:]
print(my_list)

my_list = [1, 2, 3]
my_list_copy = my_list.copy()
print(my_list, my_list_copy)

x = my_list.count(3)
print('количество вхождений в список {0}'.format(x))
x = ['привет', 'плохой', 'человек']
my_list.extend(x)
print(my_list)


x = my_list.index(2, 1, 4)
print(x)

my_list.insert(1, 'песня')
print(my_list)

print(my_list.pop(1))
print(my_list)

my_list.remove(1)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort(key=lambda a: a == 'плохой')
print(my_list)

# print(*my_list.__dir__(), sep='\n')

my_list.insert(3, 'хуй')
print(my_list)



