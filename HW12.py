
#1. Запрет ошибочного поведения на уровне интерфейса класса:

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        self.is_active = True

    def deposit(self, amount):
        if not self.is_active:
            raise ValueError("Cannot deposit to a closed account")
        self.balance += amount

    def withdraw(self, amount):
        if not self.is_active:
            raise ValueError("Cannot withdraw from a closed account")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def close_account(self):
        if self.balance != 0:
            raise ValueError("Cannot close an account with non-zero balance")
        self.is_active = False

Комментарий: В этом примере методы `deposit`, `withdraw` и `close_account` проверяют состояние счета перед выполнением операции. Это предотвращает некорректное использование методов, например, попытку внести деньги на закрытый счет или закрыть счет с ненулевым балансом.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        self.is_engine_running = False

    def start_engine(self):
        if self.is_engine_running:
            raise ValueError("Engine is already running")
        self.is_engine_running = True

    def stop_engine(self):
        if not self.is_engine_running:
            raise ValueError("Engine is not running")
        if self.speed != 0:
            raise ValueError("Cannot stop engine while the car is moving")
        self.is_engine_running = False

    def accelerate(self, delta):
        if not self.is_engine_running:
            raise ValueError("Cannot accelerate when the engine is not running")
        self.speed += delta

    def brake(self, delta):
        if self.speed - delta < 0:
            raise ValueError("Cannot brake below zero speed")
        self.speed -= delta

Комментарий: В этом примере методы `start_engine`, `stop_engine`, `accelerate` и `brake` проверяют состояние автомобиля перед выполнением действия. Это предотвращает некорректные операции, такие как попытка ускориться при выключенном двигателе или остановить двигатель во время движения.

#2. Использование обязательных аргументов в конструкторе:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

Комментарий: В этом примере конструктор класса `Rectangle` требует обязательные аргументы `width` и `height`. Это гарантирует, что объект прямоугольника всегда будет создан с корректными размерами.

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

Комментарий: В этом примере конструктор класса `User` требует обязательные аргументы `username` и `email`. Это гарантирует, что объект пользователя всегда будет создан с корректными данными.

#3. Использование прикладной системы типов:

1. Шахматная игра:

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class ChessPiece:
    def __init__(self, color, piece_type, cell):
        self.color = color
        self.piece_type = piece_type
        self.cell = cell

    def move_to(self, new_cell):
        self.cell = new_cell

# Пример использования
white_knight = ChessPiece("white", "knight", Cell(0, 1))
white_knight.move_to(Cell(2, 2))

В этом примере мы определяем классы `Cell` и `ChessPiece` для представления клетки на шахматной доске и шахматной фигуры соответственно. Вместо использования строк или чисел для представления позиции фигуры, мы используем класс `Cell`.

2. Система управления библиотекой:

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def check_out(self):
        if not self.is_available:
            raise ValueError("Book is not available for checkout")
        self.is_available = False

    def return_book(self):
        if self.is_available:
            raise ValueError("Book is already available")
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

# Пример использования
book1 = Book("Book1", "Author1", "ISBN1")
book2 = Book("Book2", "Author2", "ISBN2")

library = Library()
library.add_book(book1)
library.add_book(book2)

book1.check_out()

В этом примере мы определяем классы `Book` и `Library` для представления книги и библиотеки соответственно. Вместо использования строк для представления информации о книге, мы используем класс `Book` с соответствующими атрибутами и методами. Класс `Library` представляет коллекцию книг и предоставляет методы для управления этой коллекцией.

