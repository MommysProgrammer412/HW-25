from marvel import full_dict as fd
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

user_nums = list(map(lambda x: int(x) if x.isdigit() else None, input("Введите числа через пробел: ").split()))

new_fd = {}
for key, values in fd.items():
    new_dict = {'id': key}
    new_dict.update(values)
    new_fd[key] = new_dict

filter_dict = dict(filter(lambda x: int(x[0]) in user_nums, new_fd.items()))
