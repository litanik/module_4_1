# В модуле fake_math создаем функцию divide, которая принимает два параметра first и second
def divide(first, second):
    if second != 0:  # Если в second не записан 0,
        return first / second  # то возвращается результат деления first на second
    if second == 0:  # Если в second записан 0,
        return 'Ошибка'  # то возвращается "Ошибка"
