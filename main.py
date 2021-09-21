#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    shops = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные о магазине.
            name = input("Название магазина ")
            product = input("Товар ")
            price = int(input("Цена "))

            # Создать словарь.
            shop = {
                'name': name,
                'product': product,
                'price': price,
            }
            # Добавить словарь в список.
            shops.append(shop)
            # Отсортировать список в случае необходимости.
            if len(shops ) > 1:
                shops.sort( key = lambda item: item.get('name', '') )

        elif command == 'list':
        # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "No",
                    "Название.",
                    "Товар",
                    "Цена"
                )
            )
            print(line)
            # Вывести данные о всех сотрудниках.
            for idx, shop in enumerate(shops,1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        shop.get('name', ''),
                        shop.get('product', ''),
                        shop.get('price', 0)
                        )
                    )
                print(line)
        elif command == 'select':
            sname = input("Название магазина ")
            cout = 0
            for shop in shops:
                if(shop.get('name') == sname):
                    cout = 1
                    print(
                        ' | {:<5} | {:<5} '.format(
                            shop.get('product', ''),
                            shop.get('price', 0),
                            )
                        )
                elif cout == 0: print("Такого магазина нет")
        elif command == 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить магазин;")
                print("select - показать товары из заданного магазина;")
                print("list - вывести список магазинов;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")
        else:
                print(f"Неизвестная команда {command}", file=sys.stderr)
