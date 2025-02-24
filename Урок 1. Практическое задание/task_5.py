"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""
vyr = int(input('Ведите выручку фирмы за год: '))
izd = int(input('Ведите издержки фирмы за год: '))
res = vyr - izd
ren = vyr / izd

if vyr > izd:
    print(f"Фирма работает в прибыль.", 'Ее величина: ', res)
    print(f"Рентабильность выручки:", ren)
    sotr = int(input("Введите число сотрудников: "))
    prib1 = res / sotr
    print(f"Прибыль фирмы в расчете на одного сотрудника = ", prib1)
else: print(f"Фирма работает в убыток.", 'Его величина: ', res)