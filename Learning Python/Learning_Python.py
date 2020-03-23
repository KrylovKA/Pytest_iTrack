import sys
"""Day_1 - 23.03.2020"""
# Chapter_1(Arguments)
print('Hello World!')
var = 555  # Целое число
print(var)
var = 3.155  # Число с плавающей точкой
print(var)
var = True  # Булевая логика True/False
print(var)

semantic = 5
print(semantic*5+5)

# Chapter_2(Input)
# # Инициализируем переменную значением, введенным пользователем
# user = input('My name is Buldakov Mazafaka. What is your name?:')
# Выводим строку и значение переменной
# print('Welcome', user)

# # Инициализируем еще одну переменную значением, введенным пользователем
# user_Kirayl = input('My name is Aleksandr Buldakov Mazafaka. What is your name?:')
# # Выводим строку и значение переменной
# print('Yo', 'Ho', 'Ho,', 'Hello', user_Kirayl, sep='*', end='555')

# Chapter_3(Operators)
a = 20
b = 2
c = 5

print('Addition:\t', a, '+', b, '=', a+b)  # 3.1
print('Subtraction:\t', a, '-', b, '=', a-b)  # 3.2
print('Multiplication:\t', a, '*', b, '=', a*b)  # 3.3
print('Division:\t', a, '/', b, '=', a/b)  # 3.4
print('Floor Division:\t', a, '//', b, '=', a//b)  # 3.5
print('Modulus:\t', a, '%', b, '=', a % b)  # 3.6
print('Modulus of number:\t', a, 'abs(a)', b, '=', abs(a))  # 3.7
print('a^b for modules c:\t', a, 'pow(a,b[,c])', b, '=', pow(a, b))  # 3.8
print('Less c:\t', a, '<', b, a < b)  # 3.9
print('Less c:\t', a, '>', b, a > b)  # 3.10

print(sys.platform)
print(2**5)
x = 'Buldakov!'
print(x*8)
