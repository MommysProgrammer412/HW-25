from marvel import full_dict as fd # задание 1
from pprint import pprint
'''
1. Импортируйте full_dict из файла Marvel.py.
2. Реализуйте ввод от пользователя, который будет принимать цифры через пробел. Разбейте введённую строку на список и примените к каждому элементу int, заменяя нечисловые элементы на None с помощью map.
3. Используйте filter, чтобы создать словарь, содержащий исходные id и другие ключи, но только для тех фильмов, id которых присутствуют в списке, полученном на предыдущем шаге.
4. Создайте множество с помощью set comprehension, собрав уникальные значения ключа director из словаря.
5. С помощью dict comprehension создайте копию исходного словаря full_dict, преобразовав каждое значение 'year' в строку.
6. Используйте filter, чтобы получить словарь, содержащий только те фильмы, которые начинаются на букву Ч.
7. Отсортируйте словарь full_dict по одному параметру с использованием lambda, создавая аналогичный по структуре словарь. Обязательно укажите, по какому параметру вы производите сортировку.
8. Отсортируйте словарь full_dict по двум параметрам с использованием lambda, создавая аналогичный по структуре словарь. Обязательно укажите, по каким параметрам вы производите сортировку.
9. Опционально: Напишите однострочник, который отфильтрует и отсортирует full_dict с использованием filter и sorted.
10. Опционально: Добавьте аннотацию типов для переменных, содержащих результаты, и проверьте код с помощью mypy. Оставьте комментарий о успешной проверке.
11. Сделайте красивый вывод результатов с использованием pprint, добавив подпись о том, какое задание выполнено.
'''

user_nums = list(map(lambda x: int(x) if x.isdigit() else None, input("Задание 2. Введите числа через пробел: ").split()))# задание 2

new_fd = {}
for key, values in fd.items():
    new_dict = {'id': key}
    new_dict.update(values)
    new_fd[key] = new_dict

filter_dict = dict(filter(lambda x: int(x[0]) in user_nums, new_fd.items()))# задание 3
print('Задание 3:')
pprint(filter_dict, sort_dicts=False)
'''
1. словарь словарей c сортированными id
2. set режиссеров (? всех или из id)
4. словарь КОПИЯ fd с сторками годов
5. словарь с отфильтрованными фильмами по началу с буквы ч
6. словарь КОПИЯ fd как 5. на свое усмотрение
7. словарь КОПИЯ fd как 5. на свое усмотрение по 2 параметрам сортировки
8. pprint
'''

number_4 = set(num['director'] for num in filter_dict.values() if num['director'])#задание 4
print('Задание 4:', number_4)

number_5 = {key: {**value, 'year': str(value['year'])} for key, value in fd.items()}#задание 5
print('Задание 5:')
pprint(number_5, sort_dicts=False)

number_6 = dict(filter(lambda x: x[1].get('title') and x[1]['title'].startswith('Ч'), number_5.items()))  # задание 6
print('Задание 6:')
pprint(number_6, sort_dicts=False)

number_7 = dict(sorted(fd.items(), key=lambda item: 9999 if item[1]['year'] == 'TBA' else int(item[1]['year'])))  # задание 7: сортировка по году
print('Задание 7, сортировка по году:')
pprint(number_7, sort_dicts=False)

number_8 = dict(sorted(fd.items(), key=lambda item: (
    0 if item[1]['director'] == 'Джон Фавро' else 1, # сначала фильмы Джона Фавро
    9999 if item[1]['year'] == 'TBA' else int(item[1]['year']),# затем сортировка по году
    item[1]['director']  # сортировка по режиссеру для не-Фавро фильмов
)))# задание 8: сортировка по режиссеру (Джон Фавро в начале) и году
print('Задание 8, сортировка по режиссеру (Джон Фавро в начале) и году:')
pprint(number_8, sort_dicts=False)