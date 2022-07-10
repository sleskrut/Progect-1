# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import functools
@functools.lru_cache(maxsize= None)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('Start Pytom starter')
    print('Введение')
print('gnhtyf')
print('gnhtyf')
print('1')
print('2')
print('Переменные и типы данных')
num = 124
print (num)
b = int(num) + 5
print(b)
print(5 + True)
print(4.2e3)
x = 21
y = 5
print(x / y)
print(x // y)
math.ceil(4.2)
a = 8;
print(str(a))
c = 'g \
k'
print(c)
c = 'g \n' \
'k'
print(c)
z = list(range(10))
print(z)
print(len(z))
print(z[-1])
print(z[0:8:2])
print(8 in z)
print("ing" in "going")
print('ing' in 'went')
z.append(10)
del z[0]
print(z)
for x in z:
    print('{} ^ 3 = {}'.format(x, x ** 3))
    if x == z[9]:
     break
print('Информация по спискам удалена по ошибке')
print('Условные конструкции')
if z[8] == 9:
    print('a')
else:
    print('b')
print('c')
if z[4] == 0:
    print('d')
elif z[1] == 2:
    print('e')
else:
    print('f')
#num = int(input('Введите номер'))
#if num == 0:
   # print('zero')
#else:
    #print('not zero')
print('Функции')
def g(l):
    for i in range(l):
        print(i + 1)
g(10)
def h(j, m):
    return (j * m)
print(h(4, 5))
def red():
    kl = 8
    print(kl)
    def fgg():
        nonlocal kl
        print(kl)
        kl = kl + 1
        print(kl)
red()
def factorial(n):
    if n == 0:
        return  1
    else:
        return n * factorial(n - 1)
print(factorial(100))
print('Циклические кострукции')
t = ''
a = ''
while t != '  ':
    t = input('print ' ' to close')
    a = a + t
else:
    print('0')
print(a)
o = 3
p = ''
while o > 0:
    o -= 1
    p = input('Введите число от 1 до 10')
    if p == '1':
        print('Вы угадали число')
        break
    else:
        print('Попытайтесь ещё раз. Осталость попыток ', o)

else:
    print('Вы не угадали число')
for i in range(5, 10, 2):
    print(i**3)
for i in range(1, 10, 1):
    for j in range(1, 5, 1):
        print('1', end='')
    print()
print('Python Starter completed')









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
