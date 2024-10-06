2.3.1.

from pymonad.tools import curry

@curry(2)
def concat_strings(s1, s2):
    return s1 + s2

hello_name = concat_strings("Hello, ")

print(hello_name("John"))  # Выведет: Hello, John


2.3.2.

from pymonad.tools import curry

@curry(4)
def greet(greeting, punctuation, name, end_sign):
    return f"{greeting}{punctuation} {name}{end_sign}"

first_step = greet("Hello")(",")("!")
result = first_step("Petya")
print(result)  # Вывод: Hello, Petya!
