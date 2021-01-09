"""
СЛОВОМЕСКА
Программа загадывает слово и перемешивает в нём буквы
Задача игрока - угадать это слвоо

"""

from random import shuffle, choice

word = "ФЕВРАЛЬ"  ###Загадали слово для игры
letters = list(word)  ###Превратили строку в список отдельных букв

letter = choice(letters)
print(letter)


shuffle(letters)  ###перемешали буквы

print(*letters)  ###Вывели буквы

###ТУТ ВАШ КОД

