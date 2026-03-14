"""
Задача 3: CSV-обработка (средняя)
Создайте программу для работы с CSV-файлом products.csv:
Название  Цена Количество
Яблоки    100      50
Бананы     80      30
Молоко    120      20
Хлеб       40     100

Напишите программу, которая:
1. Считывает данные из файла
2. Позволяет пользователю добавлять новые товары
3. Поиск товара по названию
4. Расчет общей стоимости всех товаров на складе (цена × количество)
5. Сохранение обновленных данных обратно в файл
"""
import csv

FILE = "C:/Users/Валерий/Documents/PYTHON/УП2/resource3/products.csv"


def add_product(product):
    if find_product(product[0]):
        print("Продукт " + product[0] + " уже есть в списке")
        return
    with open(FILE, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(product)
    print("Продукт добавлен")


def find_product(name):
    with open(FILE, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[0] == name:
                return row


def calc_products():
    with open(FILE, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        countProducts = 0
        for row in reader:
            try:
                countProducts += float(row[1]) * int(row[2])
            except:
                continue
        return countProducts


def main():
    while True:
        print("1 - Добавить продукт")
        print("2 - Найти продукт")
        print("3 - Рассчитайте общую стоимость всех товаров")
        print("4 - Выход")
        choice = input("Введите свой выбор: ")

        match choice:
            case "1":
                try:
                    name = input("Введите название продукта: ")
                    price = float(input("Введите стоимость продукта: "))
                    count = int(input("Введите количество продуктов: "))
                    product = [name, str(price), str(count)]
                    add_product(product)
                except ValueError:
                    print("Неверный ввод")
            case "2":
                name = input("Введите название продукта: ")
                result = find_product(name)
                if result:
                    print(result)
                else:
                    print("Продукт не найден")
            case "3":
                result = calc_products()
                print(result)
            case "4":
                break
            case _:
                print("Неверный ввод")


if __name__ == "__main__":
    main()