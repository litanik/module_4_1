# Импортируем бесконечность из встроенной библиотеки math
from math import inf

# В модуле true_math создаем функцию divide, которая принимает два параметра first и second
def divide(first, second):
    if second != 0:  # Если в second не записан 0,
        return first/second  # то возвращается результат деления first на second
    if second == 0:  # Если в second записан 0,
        return inf  # то возвращается бесконечность inf
