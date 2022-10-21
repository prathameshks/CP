# forth
t = int(input())

for i in range(t):
    n, m, l = [int(i) for i in input().split()]
    for i in range(n - 1, -1, -1):
        b = i + l
        if m // b > 0:
            m = m % b
    print(m)

'''
# third
t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    c0 = a.count(0)
    c1 = a.count(1)
    c2 = a.count(2)
    if c0 > 0:
        ans += (n - c0)
        if c1 > 0:
            ans += (n - c0 - c1)
    else:
        if c1 > 0:
            ans += (n - c0 - c1)
    if c2 > 1:
        ans += ((c2 * (c2 - 1)) // 2)
    print(ans)
    
'''
'''
# second
t = int(input())

for i in range(t):
    x, y = [int(i) for i in input().split()]
    # n = input()
    if x % 2 == 1 and y % 2 == 1:
        print(-1)
    else:
        if x % 2 == 0:
            if y < 2:
                print(-1)
            else:
                print('b' + 'a' * (x // 2) + 'b' * (y - 2) + 'a' * (x // 2)+ 'b')
                print('a' * (x // 2) + 'b' * y + 'a' * (x // 2))

        elif y % 2 == 0:
            print('b' * (y // 2) + 'a' * x + 'b' * (y // 2))
            if x < 2:
                print(-1)
            else:
                print('a' + 'b' * (y // 2) + 'a' * (x - 2) + 'b' * (y // 2)+ 'a')
                print('b' * (y // 2) + 'a' * x + 'b' * (y // 2))

        else:
            if y < 2 or x < 2:
                print(-1)
            else:
                print('b' + 'a' * (x // 2) + 'b' * (y - 2) + 'a' * (x // 2)+'b')
                print('a' * (x // 2) + 'b' * y + 'a' * (x // 2))
'''
'''# first
t = int(input())

for i in range(t):
    x, y, z = [int(i) for i in input().split()]
    # n = input()
    rt = y / x
    ans = z - rt
    if ans <= 0:
        print(0)
    else:
        print(int(ans))
'''
