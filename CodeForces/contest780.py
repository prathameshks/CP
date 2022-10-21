import math

t = int(input())

for _ in range(t):
    n = int(input())
    candy = sorted(list(map(int, input().split())), reverse=True)
    # b1, b2 = map(int, input().split())
    if n <= 1 and candy[0] > 1:
        print('NO')
    else:
        a = candy[0]
        if n > 1:
            b = candy[1]
        for i in range(2, n):
            if a < b:
                a += candy[i]
                # print('a', a)
            else:
                b += candy[i]
                # print('b', b)
        if math.fabs(a - b) > 1:
            print('NO')
        else:
            print('YES')
