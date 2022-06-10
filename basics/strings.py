"================Строки=================="
# строки - тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки
# Синтаксис:
string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
# error = 'не правильная строка"
string3 = "Don't" # внутри двойных кавычек все одинарные - просто символы
string4 = '"Makers bootcamp"' # внутри одинарных кавычек все двойные - просто символы

string5 = '''
Многострочный текст 
в одинарных кавычках
Тут можно ставить "любые" 'кавычки'
"""""
'''
string6 = """
Многострочный текст 
в двойных кавычках
Тут можно ставить "любые" 'кавычки'
'''''
"""

"==============Экранизация строк==============="
# экранизаия спец-символов
'\n' # перенос на новую строку
'\t' # табуляция
'\\' # отображение \ (потому что он является инструкцией, которая влияет на наш код)
'\'' # отображение '
"\"" # отображение "
'\r' # возращение каретки в начало строки
'\v' # перенос на новую строку со смещением вправо на длину предыдущей строки

'hello\nworld' 
# hello
# world

'hello\tworld'
# hello    world

'чтобы эранировать нужен символ \\'
# чтобы эранировать нужен символ \

'My website is Latracal \rSolution'
# Solutionte is Latracal

"=============Форматирование строк================"
title = 'Плов'
price = 1300
format1 = f'Название: {title}, Цена: {price}'
# Название: Плов, Цена: 1300

format2 = 'Название: %s, Цена: %s'
print(format2 % ("Гуляш", "250"))
print(format2 % ("Самсы", "70"))
# Название: Гуляш, Цена: 250
# Название: Самсы, Цена: 70

format3 = 'Название: {}, Цена: {}'
print(format3.format('Шакарап', '35'))
# Название: Шакарап, Цена: 35