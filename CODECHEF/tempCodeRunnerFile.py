t = int(input())

for i in range(t):
    n,x = [int(i) for i in input().split()]
    # n = int(input())
    # s = input()
    if n-x > x:
        print(x)
    else:
        print(n-x)