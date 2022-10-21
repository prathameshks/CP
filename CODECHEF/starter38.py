# div 4


'''# 1
t = int(input())

for i in range(t):
    # n, x = [int(i) for i in input().split()]
    x = int(input())
    # s = input()
    if x > 30:
        print('YES')
    else:
        print('NO')

# 2
t = int(input())

for i in range(t):
    n, x, k = [int(i) for i in input().split()]
    # x = int(input())
    # s = input()
    if (n * x) > k:
        print('NO')
    else:
        print('YES')



# 3
t = int(input())

for i in range(t):
    army = [int(i) for i in input().split()]
    # x = int(input())
    # s = input()
    m=max(army)
    if m > (sum(army) - m):
        print('YES')
    else:
        print('NO')


# 4

t = int(input())

for i in range(t):
    a, b, m = [int(i) for i in input().split()]
    if a > b:
        a, b = b, a
    # x = int(input())
    # s = input()
    cw = b - a
    acw = (m - b) + a
    print(min((cw,acw)))

'''

# 5

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        a2=b[i+1:n]
        for index,elm in enumerate(a2): # a2.enum(a[i])
            if elm == a[i]:
                mi,mj =i,i+index+1
                if (a[mi] == b[mj]) and (a[mj] == b[mi]):
                    ans += 1

    print(ans)
