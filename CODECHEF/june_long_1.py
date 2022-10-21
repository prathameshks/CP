# 4

t = int(input())

for _ in range(t):
    # a,b = [int(i) for i in input().split()]
    n = int(input())
    a = input()
    b = input()
    req = set()
    for i in range(n):
        if a[i] != b[i]:
            req.add(b[i])
    # print('*',end='')
    print(len(req))

'''

# 3
t = int(input())

for _ in range(t):
    a,b = [int(i) for i in input().split()]
    # s = int(input())
    fact = b-a
    if ((fact+1) % 3) == 0:
        print('NO')
    else:
        print('YES')



# 2
t = int(input())

for _ in range(t):
    n,x = [int(i) for i in input().split()]
    # s = int(input())
    no_of_subs = n//6
    if n%6 > 0:
        no_of_subs+=1
    print(no_of_subs*x)




# 1
t = int(input())

for _ in range(t):
    x,y = [int(i) for i in input().split()]
    # s = int(input())
    if x<=y:
        print(0)
    else:
        print(x-y)

        '''