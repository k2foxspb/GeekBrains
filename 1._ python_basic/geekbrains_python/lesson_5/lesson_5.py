import time
from time import perf_counter_ns
import sys

start = perf_counter_ns()
nums = []
for num in range(1, 10 ** 6, 2):
    nums.append(num ** 2)
print('list:', perf_counter_ns() - start, type(nums), (sys.getsizeof(nums) / 100_000))

start = perf_counter_ns()
nums_gen = (num * 2 for num in range(1, 10 ** 6, 2))
print('gen:', perf_counter_ns() - start, type(nums_gen), (sys.getsizeof(nums_gen) / 100_000))


def letters_generator(start, end):
    for code in range(ord(start), ord(end) + 1):
        yield chr(code)


eng_uppercase_letters = letters_generator('A', 'Z')
print(*eng_uppercase_letters, sep='')

'''
множества
'''
chat_1 = {'user_1', 'user_5', 'user_7', 'user_8', 'user_11'}
chat_2 = {'user_1', 'user_2', 'user_2', 'user_7', 'user_9', 'user_10'}

chat_common = chat_1 & chat_2
chats_intersection = chat_1 - chat_2
chats_union = chat_1 | chat_2

print(chat_common, chats_intersection, chats_union, sep='\n')
#  неизменяемое множество
chat_1 = frozenset(('user_1', 'user_5', 'user_7', 'user_8', 'user_11'))


def gen_num(max_size):
    for num in range(0, max_size + 1):
        if num % 2 != 0:
            yield num


print(*gen_num(50))

gen_num_2 = (num for num in range(50) if num % 2 != 0)
x = next(gen_num_2)
print(x)
x = next(gen_num_2)
print(x)
x = next(gen_num_2)
print(x)
x = next(gen_num_2)
print(x)

'''
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>),
например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в
списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
кортежи в виде: (<tutor>, None), например:
('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
'''
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б',
]


def gen_tutors(tutors, klasses):
    for i in range(len(tutors)):
        if len(klasses) < len(tutors):
            klasses.append(None)
        gen = (tutors[i], klasses[i])
        yield gen


print(*gen_tutors(tutors, klasses), type(gen_tutors(tutors, klasses)), sep='\n')

'''Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
предыдущего, например:'''

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 100]
result = [12, 44, 4, 10, 78, 123, 100]
start = time.thread_time_ns()
x = (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
print(*x)

'''Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:'''

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

x = (i for i in src )

print(*x)
