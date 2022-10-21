
t = int(input())

for i in range(t):
    n, x = [int(i) for i in input().split()]
    # n = int(input())
    # s = input()
    a = []
    if n % 2 == 1:
        a.append(str(x))
    for i in range(n // 2):
        a += [str(x - i - 1), str(x + 1 + i)]

    print(' '.join(a))
