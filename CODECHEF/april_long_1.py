# 4th

t = int(input())

for i in range(t):
    n, m = [int(i) for i in input().split()]
    # n = int(input())
    s = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    arr = []
    for x in range(m):
        fact = 0
        power, cap = p[x], c[x]
        for eny in range(cap):
            if s[eny + fact] > 0:
                s[eny + fact] -= power
                if s[eny + fact] <= 0:
                    s[eny + fact] = 0
            else:
                fact += 1
                s[eny + fact] -= power
                if s[eny + fact] <= 0:
                    s[eny + fact] = 0
    print(s)

'''
# 3rd

t = int(input())

for i in range(t):
    # x, y = [int(i) for i in input().split()]
    n = int(input())
    b = (((n - 1) // 4) * 4) + 1
    for j in range(b, n + 1):
        if j & 1 == 1:
            b &= j
        else:
            b ^= j
    print(b)
    
'''

'''
# 2nd

t = int(input())

for i in range(t):
    x, y = [int(i) for i in input().split()]
    if x % 2 == 0 or x % 3 != 0:
        i = x
        j = x + 2
        if j <= y:
            print(i, j)
        else:
            print(-1)
    else:
        i = x
        j = x + 3
        if j <= y:
            print(i, j)
        else:
            print(-1)
'''
'''
# 1st

t = int(input())

for i in range(t):
    x, y = [int(i) for i in input().split()]
    # s = int(input())
    print((y - 1) // x)
'''
