t = int(input())

for i in range(t):
    # num = [int(i) for i in input().split()]
    n = int(input())-1
    if n==0:
        print(3)
    else:
        a=int('9'*n)
        print(a+3)
