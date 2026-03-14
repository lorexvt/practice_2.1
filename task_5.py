"""
Создайте систему учета книг в библиотеке. Реализуйте:
1. Хранение данных в JSON-файле library.json с информацией о книгах:
Функциональность:
1. Просмотр всех книг
2. Поиск по автору/названию
3. Добавление новой книги
4. Изменение статуса доступности (взята/возвращена)
5. Удаление книги по ID
6. Экспорт списка доступных книг в текстовый файл available_books.txt
2. Все изменения автоматически сохраняются в JSON-файл.
"""

import json

JSON_FILE = "C:/Users/Валерий/Documents/PYTHON/УП2/resource/library.json"
TXT_FILE = "C:/Users/Валерий/Documents/PYTHON/УП2/resource/available_books.txt"


def load_books():
    try:
        with open(JSON_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        initialBooks = [
            {"id": 1, "Название": "Мастер и Маргарита", "Автор": "Булгаков", "Год": 1967, "Доступ": True},
            {"id": 2, "Название": "Преступление и наказание", "Автор": "Достоевский", "Год": 1866, "Доступ": False}
        ]
        save_books(initialBooks)
        return initialBooks


def save_books(books):
    with open(JSON_FILE, 'w') as file:
        json.dump(books, file, indent=2)


def show_books(books):
    if not books:
        print("Нет доступных книг")
        return
    print(f"{'ID':<5} {'Название':<30} {'Автор':<20} {'Год':<6} {'Статус':<10}")


    for book in books:
        status = "Доступна" if book['Доступ'] else "Выдана"
        print(f"{book['id']:<5} {book['Название'][:28]:<30} {book['Автор'][:18]:<20} {book['Год']:<6} {status:<10}")



def search_book(books):
    if not books:
        print("Нет доступных книг")
        return

    query = input("Введите автора или название для поиска: ").lower()
    if not query:
        print("запрос пуст")
        return

    foundBooks = []
    for book in books:
        if query in book['Название'].lower() or query in book['Автор'].lower():
            foundBooks.append(book)

    if foundBooks:
        print(f"Найдено книг: {len(foundBooks)}")
        show_books(foundBooks)
    else:
        print(f"Книги по запросу '{query}' не найдены.")


def add(books):
    try:
        newId = max([book['id'] for book in books]) + 1 if books else 1

        title = input("Введите название книги: ")
        if not title:
            print("Название не может быть пустым!")
            return books

        author = input("Введите автора книги: ")
        if not author:
            print("Автор не может быть пустым!")
            return books

        yearStr = input("Введите год издания: ")
        if not yearStr:
            print("Год не может быть пустым!")
            return books
        year = int(yearStr)

        newBook = {
            "id": newId,
            "Название": title,
            "Автор": author,
            "Год": year,
            "Доступ": True
        }

        books.append(newBook)
        save_books(books)
    except ValueError:
        print("Год должен быть числом")
    return books


def change_status(books):
    if not books:
        print("Нет доступных книг")
        return

    try:
        bookId = int(input("Введите id книги для изменения статуса: "))

        for book in books:
            if book['id'] == bookId:
                book['Доступ'] = not book['Доступ']
                save_books(books)
                return books
    except ValueError:
        print("Id должен быть числом")


def delete_book(books):
    if not books:
        print("Нет доступных книг")
        return

    try:
        show_books(books)
        bookId = int(input("\nВведите ID книги для удаления: "))

        for book in books:
            if book['id'] == bookId:
                books.remove(book)
                save_books(books)
                return books
    except ValueError:
        print("Id должен быть числом")


def export(books):
    availableBooks = [book for book in books if book['Доступ']]

    if not availableBooks:
        print("Нет доступных книг")
        return

    with open(TXT_FILE, "w", encoding='utf-8') as file:
        for book in availableBooks:
            file.write(f"ID: {book['id']}\n")
            file.write(f"Название: {book['Название']}\n")
            file.write(f"Автор: {book['Автор']}\n")
            file.write(f"Год: {book['Год']}\n")


def main():
    books = load_books()

    while True:
        print(" " * 7, "МЕНЮ")
        print("1. Просмотр всех книг")
        print("2. Поиск по автору/названию")
        print("3. Добавление новой книги")
        print("4. Изменение статуса доступности")
        print("5. Удаление книги по ID")
        print("6. Экспорт доступных книг в файл")
        print("0. Выход")

        choice = input("Выберите действие: ")

        match choice:
            case "1":
                show_books(books)
            case "2":
                search_book(books)
            case "3":
                add(books)
            case "4":
                change_status(books)
            case "5":
                delete_book(books)
            case "6":
                export(books)
            case "0":
                break
            case _:
                print("Неверный ввод")


if __name__ == "__main__":
    main()