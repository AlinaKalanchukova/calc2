"""
Каланчукова Алина Альфредовна
редактируйте/пишите код в блоках между
---начало--- и ---конец---
Решение задачи может быть в несколько строчек, но чем меньше, тем лучше.
В случае верного решения запуск файла приведёт к выводу True для каждого задания
"""
s = 'Каланчукова Алина Альфредовна'
i = 8

""" +++ ВЛОЖЕННЫЕ СПИСКИ +++ """

""" Задание №1
Создайте пустой список 'fio'
---------------начало блока редактирования----------------"""

fio = []

"""------------ конец блока редактирования----------------"""
print('№1 ' + str(fio == []))

""" Задание №2
Используя цикл for добавьте в 'fio' список букв вашей фамилии, список букв вашего имени и список букв вашего отчества
---------------начало блока редактирования----------------"""

s = ''.join(s).split(' ')
for i in s:
    fio.append(list(i))

"""------------ конец блока редактирования----------------"""
print('№2 ' + str(fio == [['К', 'а', 'л', 'а', 'н', 'ч', 'у', 'к', 'о', 'в', 'а'], ['А', 'л', 'и', 'н', 'а'], ['А', 'л', 'ь', 'ф', 'р', 'е', 'д', 'о', 'в', 'н', 'а']]))

""" Задание №3
Используя цикл while переверните каждый элемент в 'fio' задом наперёд
---------------начало блока редактирования----------------"""

while fio:
    fio[0] = fio[0][::-1]
    fio[1] = fio[1][::-1]
    fio[2] = fio[2][::-1]
    break

"""------------ конец блока редактирования----------------"""
print('№3 ' + str(fio == [['а', 'в', 'о', 'к', 'у', 'ч', 'н', 'а', 'л', 'а', 'К'], ['а', 'н', 'и', 'л', 'А'], ['а', 'н', 'в', 'о', 'д', 'е', 'р', 'ф', 'ь', 'л', 'А']]))

""" Задание №4
Получите из переменной fio 3-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][2] 

"""------------ конец блока редактирования----------------"""
print('№4 ' + str(char == 'и'))

""" Задание №5
Получите из переменной fio 3-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][2] 

"""------------ конец блока редактирования----------------"""
print('№5 ' + str(char == 'и'))

""" Задание №6
Создайте список fio_len и запишите в него длины вашей фамилии, имени и отчества, получив их из fio
---------------начало блока редактирования----------------"""

fio_len = [len(x) for x in fio[0:3]]

"""------------ конец блока редактирования----------------"""
print('№6 ' + str(fio_len == [11, 5, 11]))

""" Задание №7
Используя стандартную функцию min получите длину самого короткого слова из ваших ФИО
---------------начало блока редактирования----------------"""

min_len = min(fio_len)

"""------------ конец блока редактирования----------------"""
print('№7 ' + str(min_len == 5))

""" Задание №8
Используя цикл в цикле получите строку, в которой будет:
последняя буква вашей фамилии, затем имени, затем отчества,
затем предпоследния буква вашей фамилии, имени, отчества,
затем предпредпоследния буква вашей фамилии, имени, отчества,
и так до того момента, пока не закончатся символы в самом коротком слове из вашей ФИО
---------------начало блока редактирования----------------"""

chars = str()
i = 0
while i < min_len:
    for l in range(len(fio)):
        chars += fio[l][i]
    i+=1

"""------------ конец блока редактирования----------------"""
print('№8 ' + str(chars == 'ааавнноивклоуАд'))


""" +++ СЛОВАРИ +++ """

""" Задание №9
Создайте словарь с ключами 'фамилия' 'имя' 'отчество' и соответствующими значениями ФИО задом наперёд
---------------начало блока редактирования----------------"""

d = dict()
d['фамилия'] = fio[0]
d['имя'] = fio[1]
d['отчество'] = fio[2]
reversed_fio_dict = d

"""------------ конец блока редактирования----------------"""
print('№9 ' + str(reversed_fio_dict == {'фамилия': ['а', 'в', 'о', 'к', 'у', 'ч', 'н', 'а', 'л', 'а', 'К'], 'имя': ['а', 'н', 'и', 'л', 'А'], 'отчество': ['а', 'н', 'в', 'о', 'д', 'е', 'р', 'ф', 'ь', 'л', 'А']}))

""" Задание №10
Получите список ключей словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_keys = list(reversed_fio_dict.keys())

"""------------ конец блока редактирования----------------"""
print('№10 ' + str(reversed_fio_dict_keys == ['фамилия', 'имя', 'отчество']))

""" Задание №11
Получите список значений словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_values = list(reversed_fio_dict.values())

"""------------ конец блока редактирования----------------"""
print('№11 ' + str(reversed_fio_dict_values == [['а', 'в', 'о', 'к', 'у', 'ч', 'н', 'а', 'л', 'а', 'К'], ['а', 'н', 'и', 'л', 'А'], ['а', 'н', 'в', 'о', 'д', 'е', 'р', 'ф', 'ь', 'л', 'А']]))

""" Задание №12
Получите список картежей, содержащий пары ключ и значение словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_items = list(reversed_fio_dict.items())

"""------------ конец блока редактирования----------------"""
print('№12 ' + str(reversed_fio_dict_items == [('фамилия', ['а', 'в', 'о', 'к', 'у', 'ч', 'н', 'а', 'л', 'а', 'К']), ('имя', ['а', 'н', 'и', 'л', 'А']), ('отчество', ['а', 'н', 'в', 'о', 'д', 'е', 'р', 'ф', 'ь', 'л', 'А'])]))

""" Задание №13
Получите значение словаря reversed_fio_dict по ключу фамилия
---------------начало блока редактирования----------------"""

res = d['фамилия']

"""------------ конец блока редактирования----------------"""
print('№13 ' + str(res == ['а', 'в', 'о', 'к', 'у', 'ч', 'н', 'а', 'л', 'а', 'К']))

""" Задание №14
Создайте пустой словарь chars
---------------начало блока редактирования----------------"""

chars = {}

"""------------ конец блока редактирования----------------"""
print('№14 ' + str(chars == {}))

""" Задание №15
Преобразуйте строку с вашей ФИО так, чтобы в ней были только маленькие буквы и отсутствовали пробелы
---------------начало блока редактирования----------------"""

s = 'Каланчукова Алина Альфредовна'
s = ''.join(s.split())
s = s.lower()

"""------------ конец блока редактирования----------------"""
print('№15 ' + str(s == 'каланчуковаалинаальфредовна'))

""" Задание №16
Пройдите в цикле по всем буквам своих ФИО 's' и сосчитайте количество повторений каждой буквы.
Получите список 'res' из пар (кортежей):
( <буква вашей ФИО>, <количество её появления в вашей ФИО> )
---------------начало блока редактирования----------------"""

res = {}

for i in s:
    res[i] = s.count(i)
res = list(res.items())

"""------------ конец блока редактирования----------------"""
print('№16 ' + str(res == [('к', 2), ('а', 7), ('л', 3), ('н', 3), ('ч', 1), ('у', 1), ('о', 2), ('в', 2), ('и', 1), ('ь', 1), ('ф', 1), ('р', 1), ('е', 1), ('д', 1)]))


""" +++ ФУНКЦИИ +++ """

""" Задание №17
Напишите функцию alinaCharToIndex которая:
- получает на вход букву русского алфавита,
- возвращает её номер в алфавите (от 1 до 33).
Например вызов alinaCharToIndex('А') должен возвращать 1
---------------начало блока редактирования----------------"""

def alinaCharToIndex(letter):

    alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

    return alphabet.index(letter)+1

"""------------ конец блока редактирования----------------"""
print('№17 ' + str(alinaCharToIndex("Ч") == 25))

""" Задание №18
При помощи функции alinaCharToIndex измените fio так, чтобы вместо букв, в нём были их номера в алфавите
---------------начало блока редактирования----------------"""

fio

"""------------ конец блока редактирования----------------"""
print('№18 ' + str(fio == [[1, 3, 16, 12, 21, 25, 15, 1, 13, 1, 12], [1, 15, 10, 13, 1], [1, 15, 3, 16, 5, 6, 18, 22, 30, 13, 1]]))


""" +++ КОНЕЦ =) +++ """
