# вариант 4
import matplotlib.pyplot as graf
import numpy as np


AMOUNT = 250


def white(text):
    print('\033[1;2;47m {}\033[0m' .format(text))


def red(text):
    print('\033[41m {}\033[0m' .format(text))


white(6*'\t ')
white(6*'\t ')
red(6*'\t ')
red(6*'\t ')


print('\n\033[44m', 6*'\t ', '\033[0m')
print(10*' ', '\033[44m   \033[0m')
print('\033[44m', 6*'\t ', '\033[0m ')
print(4*' ', '\033[44m  ', 9*'\033[0m ', '\033[44m   \033[0m')
print('\033[44m', 6*'\t ', '\033[0m')


fig, AX = graf.subplots()
X = np.linspace(0, 100, 1000)
Y = np.sqrt(X)
AX = AX.plot(X, Y)
graf.show()


with open('sequence.txt') as f:
    first125 = 0
    sec125 = 0
    for i in range(125):
        first125 += float(f.readline())
    for i in range(125):
        sec125 += float(f.readline())
    first125 = first125/AMOUNT*100
    sec125 = sec125/AMOUNT*100
    names = ['ср знач первых 125', 'зр знач вторых 125']
    values = [first125, sec125]
    graf.bar(names, values)
    graf.show()
