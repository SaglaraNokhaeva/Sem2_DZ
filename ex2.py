#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.


import fractions
a = input('Введите первую дробь в формате: a/b: ')
a_numerator = int(a.split("/")[0])
a_denominator =int(a.split("/")[1])
b = input('Введите вторую дробь в формате: a/b: ')
b_numerator = int(b.split("/")[0])
b_denominator =int(b.split("/")[1])


# НАХОЖДЕНИЕ СУММЫ ДВУХ ДРОБЕЙ:
# Нахождение общего знаменателя
if a_denominator > b_denominator:
    greater = a_denominator
else:
    greater = b_denominator

while True:
    if((greater % a_denominator == 0) and (greater % b_denominator == 0)):
        add_denominator = greater
        break
    greater += 1

# Нахождение дополнительных множителей
a_additional_multiplier = add_denominator/a_denominator
b_additional_multiplier = add_denominator/b_denominator

# Нахождение числителя суммы
add_numerator = int(a_numerator*a_additional_multiplier + b_numerator*b_additional_multiplier)

# Приведение результата к несократимой дроби
if add_numerator < add_denominator:
    smallest = add_numerator
else:
    smallest = add_denominator
for i in range(1, smallest + 1):
        if(( add_numerator % i == 0) and(add_denominator % i == 0 )):
            NOD = i
add_numerator = int(add_numerator/NOD)
add_denominator = int(add_denominator/NOD)
print('Сумма = ', add_numerator,"/", add_denominator)

# НАХОЖДЕНИЕ ПРОИЗВЕДЕНИЯ ДВУХ ДРОБЕЙ:
multiplier_numerator = a_numerator*b_numerator
multiplier_denominator = a_denominator*b_denominator

# Приведение результата к несократимой дроби
if multiplier_numerator < multiplier_denominator:
    smallest = multiplier_numerator
else:
    smallest = multiplier_denominator
for i in range(1, smallest + 1):
        if(( multiplier_numerator % i == 0) and(multiplier_denominator % i == 0 )):
            NOD = i
multiplier_numerator = int(multiplier_numerator/NOD)
multiplier_denominator = int(multiplier_denominator/NOD)
print('Произвдение = ', multiplier_numerator,"/", multiplier_denominator)

# Проверка
print('Проверка')
f1 = fractions.Fraction(a_numerator, a_denominator)
f2 = fractions.Fraction(b_numerator, b_denominator)
print('Сумма = ',f1 + f2)
print('Произвдение = ', f1 * f2)
