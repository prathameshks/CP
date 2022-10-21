t = int(input())

for i in range(t):
    n, x, y = [int(i) for i in input().split()]
    # n = int(input())
    s = input()
    if '1' not in s or '0' not in s:
        print(0)
    else:
        print(min(x, y))
