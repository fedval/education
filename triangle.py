from turtle import *

for i in range(3):
    forward(100)
    right(120)

for i in range(12):
    print(i, end=' ')

for i in range(1, 16, 3):
    print(i, end='  ')

for i in range(11, -2, -1):
    print(i, end='    ')

n = 3
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(b, 'x', a, '=', b * a)
