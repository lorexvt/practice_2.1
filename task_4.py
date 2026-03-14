"""
Напишите программу-калькулятор с логированием:
1. Программа запрашивает у пользователя два числа и операцию (+, -, *,
/)
2. Выполняет вычисление
3. Записывает каждую операцию в файл calculator.log в формате:
Пример:
[2024-01-20 14:30:25] 10 + 5 = 15
[2024-01-20 14:31:10] 8 * 3 = 24
4. При запуске программы показывать последние 5 операций из логфайла
5. Реализовать возможность очистки лог-файла
"""
from datetime import datetime

LOG_FILE = "/УП2/resource/calculator.txt"


def last_operations(filename=LOG_FILE):
    try:
        with open(filename,"r") as f:
            lines = f.readlines()
            lastLines = lines[-5:] if len(lines) > 5 else lines

            print("История операций")
            if lastLines:
                for op in lastLines:
                    print(op.strip())
            else:
                print("Никаких последних операций")
            print()
    except FileNotFoundError:
        print("Файл не найден")


def file_clear(filename=LOG_FILE):
    with open(filename, 'w') as f:
        f.write("")


def write_file(expression, filename=LOG_FILE):
    with open(filename,"a") as f:
        currentDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{currentDate}] {expression}\n")


def calc(x, y, operator):
    if operator == "+":
        return f"{x} + {y} = {x + y}"
    elif operator == "-":
        return f"{x} - {y} = {x - y}"
    elif operator == "*":
        return f"{x} * {y} = {x * y}"
    elif operator == "/":
        if y == 0:
            raise ValueError("Деление на ноль")
        else:
            return f"{x} / {y} = {x / y}"
    else:
        raise ValueError(f"Неизвестный оператор {operator}")


def main():

    last_operations()

    while True:
        print("1 - Вычислить")
        print("2 - Очистить файл")
        print("3 - Выход")
        choice = input("Введите свой выбор: ")

        match choice:
            case "1":
                try:
                    num1 = float(input("Введите первое число: "))
                    num2 = float(input("Введите второе число: "))
                    operator = input("Введите оператора (+, -, *, /): ")

                    if operator not in ["+", "-", "*", "/"]:
                        raise ValueError("Неверный оператор")

                    result = calc(num1, num2, operator)
                    if result:
                        write_file(result)
                except ValueError as e:
                    print(f"{e}")
                except Exception as e:
                    print(f"{e}")
            case "2":
                file_clear()
            case "3":
                break
            case _:
                print("Неверный выбор")


if __name__ == "__main__":
    main()