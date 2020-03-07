#!/bin/env python3

import sys
from shutil import get_terminal_size
from collections import deque

terminal_size = get_terminal_size()


def half2full(s):
    return s.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))


try:
    s = sys.argv[1]
except IndexError:
    print('usage: echo-tategaki.py [text]')
    exit(1)


s = half2full(s)

col = terminal_size.columns // 3
col_sp = terminal_size.columns % 3
line = terminal_size.lines - 4

a = [['　' for i in range(col)] for j in range(line)]

p = 0
m = len(s)

j = col - 1
while j > 0:
    i = 0
    while i < line:
        c = s[p]
        p += 1
        if c == '\n':
            j -= 1
            i = 0
            continue
        if c == '\r':
            i = 0
            continue
        a[i][j] = c
        if p >= m:
            break
        i += 1
    else:
        j -= 1
        continue
    break

if not all([all([j == '　' for j in i]) for i in a]):
    while all([i[0] == '　' for i in a]):
        for i in range(len(a)):
            ii = deque(a[i])
            ii.rotate(-1)
            a[i] = list(ii)

for i in a:
    print(' ' * col_sp + ' '.join(i))

