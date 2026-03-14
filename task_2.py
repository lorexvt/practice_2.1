"""
Задача 2: Фильтрация данных (средняя)
Дан файл students.txt со списком студентов и их оценками в формате:
text
Иванов Иван:5,4,3,5
Петров Петр:4,3,4,4
Сидорова Мария:5,5,5,5
Напишите программу, которая:
1. Читает файл
2. Рассчитывает средний балл для каждого студента
3. Записывает в новый файл result.txt только студентов со средним
баллом выше 4.0
4. Выводит на экран студента с наивысшим средним баллом
"""

#ЧТЕНИЕ ФАЙЛА
def readFile(filename):
    try:
        my_file = open(filename, "r", encoding="utf-8")
        my_text = my_file.read()
        my_file.close()
        return my_text
    except:
        print("Не удалось прочитать файл")


#СР БАЛЛ
def averagePoints(filename):
    try:
        my_file = open(filename, "r", encoding="utf-8")
        averagePointsList = []
        while True:
            line = my_file.readline()
            if line != "":
                new_line = line.strip().split(":")
                numbers = new_line[-1].split(",")
                if new_line[-1] == "text":
                    continue
                averagePointsList.append((int(numbers[0]) + int(numbers[1]) + int(numbers[2]) + int(numbers[3])) / 4)
            else:
                break
        my_file.close()
        return averagePointsList
    except:
        print("Не удалось открыть файл")


#ДОБАВ ИМЁН
def userName(filename):
    my_file = open(filename, "r", encoding="utf-8")
    users = []
    while True:
        line = my_file.readline()
        if line != "":
            new_line = line.strip().split(":")
            numbers = new_line[-1].split(",")
            if new_line[-1] == "text":
                continue
            users.append(new_line[0])
        else:
            break
    my_file.close()
    return users


#ДОБАВ ЗНАЧ
def my_dictonary(filename):
    users = userName(filename)
    averages = averagePoints(filename)
    my_dict = {}
    for i in range(len(users)):
        my_dict[users[i]] = averages[i]
    return my_dict


#ЗАПИСЬ В RESULT
def writeToFile(filename, my_dict):
    try:
        my_file = open(filename, "w", encoding="utf-8")
        for name, avg in my_dict.items():
            if avg > 4.0:
                my_file.write(f"{name}: {avg}\n")
        my_file.close()
    except:
        print("Не удалось открыть файл")


#ПОИСК ТОП СТУДЕНТА
def findTopStudent(my_dict):
    top_student = max(my_dict, key=my_dict.get)
    top_avg = my_dict[top_student]

    print("\nСтудент с наивысшим средним баллом:", top_student)
    print("Средний балл:", top_avg)
    return top_student, top_avg


#ГЛАВ ФУНКЦИЯ
def main():
    readFile("C:/Users/Валерий/Documents/PYTHON/УП2/resource/students.txt")
    print(averagePoints("C:/Users/Валерий/Documents/PYTHON/УП2/resource/students.txt"))
    print(userName("C:/Users/Валерий/Documents/PYTHON/УП2/resource/students.txt"))
    print(my_dictonary("C:/Users/Валерий/Documents/PYTHON/УП2/resource/students.txt"))
    writeToFile("C:/Users/Валерий/Documents/PYTHON/УП2/resource/result.txt", my_dictonary("C:/Users/Валерий/Documents/PYTHON/УП2/resource/students.txt"))
    findTopStudent(my_dictonary("C:/Users/Валерий/Documents/PYTHON/УП2/resource/students.txt"))


if __name__ == "__main__":
    main()





