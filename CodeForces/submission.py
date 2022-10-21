t=int(input())
for i in range(t):
    # n=int(input())
    n,q = [int(x) for x in input().split()]
    steps = [int(x) for x in input().split()]
    ques = [int(x) for x in input().split()]
    for que in ques:
        ans = 0
        k=0
        for step in steps:
            if step<=que:
                ans+=step
            else:
                break
        print(ans,end=" ")
    print()

exit()


t=int(input())
for i in range(t):
    # n=int(input())
    a,b = input().split()
    if a[-1] == 'S':
        lasta = 0
    elif a[-1] == 'M':
        lasta = 1
    else:
        lasta = 2

    if b[-1] == 'S':
        lastb = 0
    elif b[-1] == 'M':
        lastb = 1
    else:
        lastb = 2

    rca = len(a[0:-1])
    rcb = len(b[0:-1])
    
    if lasta>lastb:
        print(">")
    elif lasta<lastb:
        print("<")
    else:
        if lastb == 0:
            if (rca > rcb):
                print("<")
            elif(rca < rcb):
                print(">")
            else:
                print("=")
                    
        elif lastb == 2:
            if (rca > rcb):
                print(">")
            elif(rca < rcb):
                print("<")
            else:
                print("=")
        else:
            print("=")


def is_prime(num):
    if num<2:
        return False
    if (num%2 == 0 and num!=2):
        return False
    for i in range(3,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True


t=int(input())
for i in range(t):
    n=int(input())
    arr = [int(a) for a in input().split()]

    mi = -1
    for j in range(n):
        for k in range(n):
            if (is_prime(arr[j]+arr[k]) and (j+k+2)>mi):
                mi = j+k+2
    print(mi)



t=int(input())
for i in range(t):
    n=int(input())
    arr = [int(a) for a in input().split()]
    res = []
    flag = 0
    for j in arr:
        if j not in res:
            res.append(j)
        else:
            flag = 1
            break
    if flag == 0:
        print("YES")
    else:
        print("NO")