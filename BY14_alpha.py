import math
# импорт модуля для работы с числами и расчетами


hello_msg = ('Привет! Я Альфа версия программы для расчета справки ВУ-14, для грузового состава 4-х осных вагонов.\n'
             'Пока я умею только считать по данным что вы мне передаете, но в будущем\n'
             'я обзаведусь искусственным интеллектом, машинным зрением;)\n'
             'и вам будет достаточно отправить фото с данными состава, а я все сделаю сама\n'
             'Но пока посчитаем по простому, нанчем?)')
# просто приветственное сообщение с небольшим анонсом будущих возможностей

print(hello_msg)
# вывод приветственного сообщения



weight = input("Введите вес состава: ")
# получение веса состава
pressing = input("Нажатие (33, 44, 55): ")
# получение нажатия
axis = input("Количество осей: ")
# получение количества осей
laden = input("Количесто груженых: ")
# получение количества груженых вагонов
empty = input("Количество порожних: ")
# получение количества порожних вагонов


weight = int(weight)
pressing = int(pressing)
axis = int(axis)
laden = int(laden)
empty = int(empty)
# приведение всех полученных данных к типу int

if pressing == 33:
    necessary = weight * 0.33
    print (necessary)
elif pressing == 44:
    necessary = weight * 0.44
    print (necessary)
else:
    necessary = weight * 0.55
    print(necessary)
# расчет потребного нажатия


if laden == 0:
    necessary_fact = 4 * empty * 3.5
    print (necessary_fact)
elif empty == 0:
    necessary_fact = 4 * laden * 7
    print(necessary_fact)
else:
    necessary_fact = 4 * laden * 7 + 4 * empty * 3.5
    print(necessary_fact)


print('Потребное нажатие: ' + str(necessary) + ' тс')
print('Фактическое нажатие: ' + str(necessary_fact) + ' тс')
