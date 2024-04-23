# Anatoli Gutovski
# Homework-6
# 09.04.2024
# Grodno-IT-Academy-Python 3.11.7


# Создайте  модель из жизни. Это может быть бронирование комнаты в отеле, покупка билета в транспортной компании, или простая РПГ. Создайте несколько объектов классов, которые описывают ситуацию. Объекты должны содержать как атрибуты так и методы класса для симуляции различных действий. Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать методы, взаимодействие объектов и т.д.

"""
Управление банковским счетом

Вначале создадим класс BankAccount, представляющий банковский счет.
Атрибуты могут включать баланс, номер счета и владельца.
Методы могут включать пополнение счета, снятие денег и проверку баланса.
"""


import pytest
from your_module import prime_number, sum_of_primes_n
# Не вижу этот модуль

# Эта строка объявляет класс с именем BankAccount
class BankAccount:
    # Это метод-конструктор класса BankAccount
    def __init__(self, account_number, vladelec):
        self.account_number = account_number
        self.vladelec = vladelec
        # Начальное значение баланса принимаем 0
        self.balance = 0

    # Это метод класса BankAccount, который принимает один аргумент amount
    def deposit(self, amount):
        # Метод увеличивает баланс счета на указанную сумму amount
        self.balance += amount

    # Это метод класса BankAccount, который принимает один аргумент amount
    def withdraw(self, amount):
        # Метод уменьшает баланс счета на указанную сумму amount
        self.balance -= amount


account1 = BankAccount("007737", "John Ataman")
account2 = BankAccount("135091", "Alex Huracan")
# Окей, но в условии задачи было создание нескольких классов, их взаимодействие, какая-то логика, тут просто определение одного класса

# Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без исключений (но не более n раз - параметр декоратора). Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors


# Здесь определяется новый класс исключения TooManyErrors, который наследуется от встроенного класса Exception
class TooManyErrors(Exception):
    pass


def retry(n):
    # Здесь определяется внутренняя функция decorator, которая принимает функцию func в качестве аргумента
    def decorator(func):
        # Здесь определяется внутренняя функция wrapper, которая принимает произвольное количество позиционных и именованных аргументов
        def wrapper(*args, **kwargs):
            # Создадим переменную attempts и присвоим значением 0
            attempts = 0
            # Цикл while, который будет выполняться до тех пор, пока количество попыток не превысит значение n
            while attempts < n:
                try:
                    # Вызывается оригинальная функция с переданными аргументами, и её результат возвращается
                    return func(*args, **kwargs)
                # Если в блоке try происходит исключение, оно перехватывается, и его информация сохраняется в переменной e
                except Exception as e:
                    attempts += 1
            # Если количество попыток выполнения превышает значение n, выбрасывается исключение TooManyErrors
            raise TooManyErrors(
                f"Function {func.__name__} failed after {n} attempts")
        # Возвращается внутренняя функция wrapper, которая теперь содержит логику повторного выполнения функции
        return wrapper
    return decorator
    # Тут верно

# Пример функции, которая выбрасывает исключение:

@retry(2)
def bad_function():
    # Внутри функции bad_function выбрасывается исключение
    raise ValueError("Something went wrong")


bad_function()  # Выдает TooManyErrors после двух попыток
# Окей

# Выберите себе две задачи по ссылке: https://euler.jakumo.org/problems/pg/1.html Решите ее в виде функции и покройте тестами. Учтите, что в функцию могут быть переданы некорректные значения, здесь может пригодится ‘assertRaises’.
# Напиши около 7-10 условий для теста.
# Постарайтесь брать задачи, которые мы не разбирали на занятии. Попробуйте написать максимально  «заковыристые» тесты, которые попытаются сломать ваше решение.


"""
1-ая задача, решение через функцию

Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
"""

# Определение функции prime_number, которая принимает один аргумент num


def prime_number(num):
    # Условие проверяет, если число num меньше 2, то функция возвращает False, так как простые числа начинаются с 2
    if num < 2:
        return False
    # Цикл for, который перебирает значения от 2 до квадратного корня из num плюс 1
    for i in range(2, int(num**0.5) + 1):
        # Условие проверяет, если число num делится на i без остатка, то есть num не является простым числом
        if num % i == 0:
            # Возвращается значение False, если число num делится на i без остатка
            return False
    # Если число не делится нацело ни на одно из значений в цикле, то возвращается значение True
    return True


def sum_of_primes_n(n):
    # Создадим переменную prime_sum и присвоим значение 0
    prime_sum = 0
    # Цикл for, который перебирает значения от 2 до n (не включительно)
    for i in range(2, n):
        # Условие проверяет, является ли текущее значение i простым числом, используя функцию prime_number
        if prime_number(i):
            # Если число i является простым, то оно добавляется к переменной prime_sum
            prime_sum += i
    # Возвращается общая сумма всех простых чисел до значения n
    return prime_sum


# Тесты

def test_is_prime():
    assert prime_number(0) == False
    assert prime_number(1) == False
    assert prime_number(2) == True
    assert prime_number(3) == True
    assert prime_number(4) == False
    assert prime_number(5) == True
    assert prime_number(6) == False


def test_sum_of_primes_below_n():
    assert sum_of_primes_n(10) == 17  # 2 + 3 + 5 + 7 = 17
    assert sum_of_primes_n(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77
    # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 = 129
    assert sum_of_primes_n(30) == 129
    assert sum_of_primes_n(1) == 0
    assert sum_of_primes_n(2) == 0
    assert sum_of_primes_n(3) == 2
    assert sum_of_primes_n(100) == 1060


if __name__ == "__main__":
    pytest.main()
# Окей, но тесты хотелось бы более сложные, не просто проверка вычисления - проверки типов аргументов, отлавливание исключений и пр

"""
2-ая задача, решение через функцию

Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом?
"""

# Определение функции prime_number, которая принимает один аргумент num


def prime_number(num):
    # Условие проверяет, если число num меньше 2, то функция возвращает False, так как простые числа начинаются с 2.
    if num < 2:
        return False
    # Цикл for, который перебирает значения от 2 до квадратного корня из num плюс 1
    for i in range(2, int(num**0.5) + 1):
        # Условие проверяет, если число num делится на i без остатка, то есть num не является простым числом
        if num % i == 0:
            # Возвращается значение False, если число num делится на i без остатка
            return False
    # Если число не делится нацело ни на одно из значений в цикле, то возвращается значение True
    return True


# Определение функции n_prime_number, которая принимает один аргумент n
def n_prime_number(n):
    # Создадим переменную prime_count и присвоим значение 0
    prime_count = 0
    # Создадим переменную num и присвоим значение 2
    num = 2
    # Цикл будет выполняться до тех пор, пока не будет найдено n-ное простое число
    while True:
        # Условие проверяет, является ли текущее значение num простым числом, используя функцию prime_number
        if prime_number(num):
            # Если число num является простым, увеличивается счетчик найденных простых чисел
            prime_count += 1
            # Условие проверяет, если количество найденных простых чисел равно заданному значению n
            if prime_count == n:
                return num
        # Если текущее число не является простым или не достигнуто нужное количество простых чисел, увеличивается значение переменной num для проверки следующего числа
        num += 1


# Тесты

def test_first_prime():
    assert n_prime_number(1) == 2


def test_third_prime():
    assert n_prime_number(3) == 5


def test_large_prime():
    assert n_prime_number(50) == 229
# Та же история про тесты
