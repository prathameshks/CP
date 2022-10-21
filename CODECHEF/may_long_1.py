# div 4

# 4

t = int(input())

for i in range(t):
    n, x, y = [int(i) for i in input().split()]
    ans = 2 * (n - 1)
    a, b = x, y
    a -= 1
    b -= 1
    while a > 0 and b > 0:
        a -= 1
        b -= 1
        ans += 1
    a -= 1
    b += 1
    while a > 0 and b > 0:
        a -= 1
        b += 1
        ans += 1

'''
# 3

t = int(input())

for i in range(t):
    # x, y = [int(i) for i in input().split()]
    n = int(input())
    print(n*15)


# 2

t = int(input())

for i in range(t):
    x, y = [int(i) for i in input().split()]
    # n = int(input())
    req = (x * 107) / 100
    if y <= req:
        print('YES')
    else:
        print('NO')


# 1

t = int(input())

for i in range(t):
    x, y = [int(i) for i in input().split()]
    # n = int(input())
    # s = [int(i) for i in input().split()]
    if x >= 1 and x == y:
        print('YES')
    else:
        print('NO')
'''
