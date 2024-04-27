1. 
Управление ресурсами (файлы, соединения с базой данных и т.д.):
Абстракция: Контекстный менеджер (with statement)

Описание: Контекстный менеджер позволяет автоматически управлять жизненным циклом ресурса, гарантируя его корректное закрытие после использования. 
Это избавляет от необходимости явно закрывать ресурс в блоке finally.

Было:

file = open('data.txt', 'r')
try:
    data = file.read()
    # обработка данных
finally:
    file.close()

conn = connect_to_database()
try:
    cursor = conn.cursor()
    # выполнение запросов
finally:
    cursor.close()
    conn.close()

Стало:

with open('data.txt', 'r') as file:
    data = file.read()
    # обработка данных

with connect_to_database() as conn:
    with conn.cursor() as cursor:
        # выполнение запросов
        
        
2.
Обработка исключений:
Абстракция: Декоратор для обработки исключений

Описание: Декоратор позволяет вынести логику обработки исключений из функции, сделав код более чистым и читаемым. 
Декоратор оборачивает функцию и перехватывает исключения, возникающие при её выполнении.

Было:

def process_data(data):
    try:
        result = do_something_with_data(data)
    except ValueError as e:
        logger.error(f"Ошибка обработки данных: {e}")
        result = None
    return result

def another_function(value):
    try:
        result = do_something_else(value)
    except ValueError as e:
        logger.error(f"Ошибка в another_function: {e}")
        result = None
    return result

Стало:

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            logger.error(f"Ошибка: {e}")
            return None
    return wrapper

@handle_exceptions
def process_data(data):
    return do_something_with_data(data)

@handle_exceptions
def another_function(value):
    return do_something_else(value)
    

3.
Инициализация и очистка состояния:
Абстракция: Класс с методами enter и exit (для использования с with statement)

Описание: Создание класса, реализующего протокол контекстного менеджера, позволяет инкапсулировать логику инициализации и очистки состояния. 
Это делает код более модульным и повторно используемым.

Было:

state1 = initialize_state1()
try:
    # использование состояния 1
    result1 = do_something_with_state1(state1)
finally:
    cleanup_state1(state1)

state2 = initialize_state2()
try:
    # использование состояния 2
    result2 = do_something_with_state2(state2)
finally:
    cleanup_state2(state2)

Стало:

class StateManager:
    def __init__(self, initializer, cleanup):
        self.initializer = initializer
        self.cleanup = cleanup

    def __enter__(self):
        self.state = self.initializer()
        return self.state

    def __exit__(self, exc_type, exc_value, traceback):
        self.cleanup(self.state)

with StateManager(initialize_state1, cleanup_state1) as state1:
    # использование состояния 1
    result1 = do_something_with_state1(state1)

with StateManager(initialize_state2, cleanup_state2) as state2:
    # использование состояния 2
    result2 = do_something_with_state2(state2)
Использование класса StateManager с методами enter и exit позволяет инкапсулировать логику инициализации и очистки состояния. 
Класс принимает функции инициализации и очистки в качестве аргументов конструктора. 
Метод enter вызывается при входе в with и выполняет инициализацию состояния. 
Метод exit вызывается при выходе из with и выполняет очистку состояния.








