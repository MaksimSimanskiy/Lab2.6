#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school= {'1a':14,'3b':29,'6d':12,'3f':39,'5a':34}
    num = input("Добавьте класс ")
    qunt = input("Количество человек в классе ")
    school.setdefault(num, qunt)
    num2 = input ("Удалить класс ")
    school.pop(num2)
    num3 = input("Выбрать класс для изменения ")
    num4 = input("Новое количество человек ")
    school[num3] = num4
    summ = 0
for key, value in school.items():
    print(key, 'is', value)
    summ = summ + int(value)
print("Количество человек ",summ)