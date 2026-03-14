"""
Задача 1: Базовый анализ текста
Напишите программу, которая:
1. Создает файл text.txt и записывает в него 5 строк текста (любых)
2. Читает файл и выводит:
1. Количество строк в файле
2. Количество слов в файле
3. Самую длинную строку
"""

#СОЗДАНИЕ ФАЙЛА И ВВОД СТРОК
def create_file(filename):
    try:
        my_file = open(filename, "w")
        for i in range(5):
            my_file.write(input("Введите строку " + str(i + 1) + ": ") + "\n")
        my_file.close()
    except:
        print("Не удалось создать файл!")


#КОЛ-ВО СТРОК
def counter_lines(filename):
    try:
        count = 0
        my_file = open(filename, "r")
        while True:
            line = my_file.readline()
            if line != "":
                count += 1
            else:
                break
        my_file.close()
        return count
    except:
        print("Не удалось открыть файл!")


#КОЛ-ВО СЛОВ
def counter_words(filename):
    try:
        my_file = open(filename, "r")
        my_text = my_file.read()
        words = my_text.split()
        total_words = len(words)
    except:
        print("Не удалось открыть файл!")
    return total_words


#САМАЯ ДЛИННАЯ СТРОКА
def longest_line(filename):
    try:
        biggest = ""
        my_file = open(filename, "r")
        while True:
            line = my_file.readline()
            if line != "":
                if len(line) > len(biggest):
                    biggest = line
            else:
                break
        my_file.close()
        return biggest
    except:
        print("Не удалось открыть файл!")


#ГЛАВ ФУНКЦИЯ
def main():
    create_file("../resource/text.txt")
    print("Кол-во строк в файле:", counter_lines("../resource/text.txt"))
    print("Кол-во слов в файле:", counter_words("../resource/text.txt"))
    print("Самая длинная строка:", longest_line("../resource/text.txt"))


if __name__ == '__main__':
    main()

