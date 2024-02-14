
'''Поиск подстроки в строке. Возвращает номер первого вхождения или -1'''
s = 'hello world'
print(s.find('o w', 1, 7))
print(s)

'''Поиск подстроки в строке.
 Возвращает номер первого вхождения или вызывает ValueError'''
print(s.index('wo'))

'''Замена шаблона на замену. maxcount ограничивает количество замен'''
print(s.replace('l', 'W'))
print(s)
print(s.split('l'))
print(s)
print(ord('р'), chr(1088))

print(s.rpartition('lo'))








