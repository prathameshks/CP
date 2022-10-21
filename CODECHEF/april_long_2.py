#4

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    c1 = a.count(1)
    c_1 = a.count(-1)
    if c1/2 <= c_1+1:
        print('YES')
    else:
        print('NO')
    # print(c1,c_1)




# 5

# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     a = [int(i) for i in input().split()]
#     mean = sum(a) / n
#     sumof2 = mean * 2
#     c = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if a[i] + a[j] == sumof2:
#                 c += 1
#     print(c)

# 3
'''
t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    count = 0
    if a == sorted(a):
        print('YES')

    else:
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                count += 1
                if count > 1:
                    print('NO')
                    break
        else:
            print('YES')
'''
'''
# 2

t = int(input())

for i in range(t):
    a, b = [int(i) for i in input().split()]
    # n = int(input())
    aa = a * 2
    if aa > b:
        print("FIRST")
    elif b > aa:
        print('SECOND')
    else:
        print('ANY')'''

'''
# 1

t = int(input())

for i in range(t):
    # n, m = [int(i) for i in input().split()]
    n = int(input())
    if n > 1000:
        print(n // 10)
    else:
        print(100)
'''
