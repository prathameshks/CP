from typing import *


def make(s):
    a = []
    old = 2
    for i in s:
        # c = 0
        if i == old:
            a[-1] += 1
        else:
            # c += 1
            old = i
            a.append(1)
    return a


def test(s: str) -> int:
    # Write your code here.
    cur = int(s[0])
    sl = make(s)
    arr = [0]
    first = False
    for i in sl:
        if cur == 1:
            if first:
                fact = 0
                first = False
                arr.extend([p for p in range(i)])
            else:
                fact = arr[-1]
                arr.extend([p for p in range(fact + 1, i + fact + 1)])
            # print('1here',arr)
            cur = 0
        else:
            arr.extend([q for q in range(i, -1, -1)])
            cur = 1
    print(arr)
    return sum(arr)


print(test('100'))
