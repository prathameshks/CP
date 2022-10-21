t = int(input())

for i in range(t):
    # n,x=[int(i) for i in input().split()]
    n = int(input())
    # s = input()

    ans = 1
    c = 0
    while ans < n:
        c += 1
        ans = ans * 2 + 1
    else:
        print(n - c - 1)
