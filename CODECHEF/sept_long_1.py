'''t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    strength = []
    for i in range(n):
        g=0
        gs,ws = a[i],b[i]
        # print('$',gs,ws)
        for j in range(n):
            if a[j]<gs or b[j]<ws:
                g+=1
        # print('@',g)
        strength.append(g)
    print(strength.count(max(strength)))

'''








import math


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    min_val = min(a)
    max_val = max(a)
    if min_val<0 and max_val>0:
        ans_min = min_val*max_val
    elif min_val<0 and max_val<0:
        if 0 in a:
            ans_min = 0
        else:
            ans_min = max_val*max_val
    else:
        ans_min = min_val*min_val
    if abs(min_val)>abs(max_val):
        ans_max = min_val*min_val
    else:
        ans_max = max_val*max_val

    print(ans_min,ans_max)



exit()

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    min2=max2 = a[0]
    for i in a:
        if i > max2:
            # max1 = max2
            max2 = i
        if i < min2:
            # min1 = min2
            min2 = i
    # max1 = max(a)
    # a.remove(max1)
    # max2 = max(a)
    # min1 = min(a)
    # a.remove(min1)
    # min2 = min(a) 
    print(min2*min2,max2*max2)


exit()


t = int(input())
def sum1(n):
    res = n*(n-1)
    return res/2
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    d = {}
    ans = 0
    for i in a:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i]+=1
    for j in d.values():
        ans+= int(sum1(j))
    print(ans)




t = int(input())

for _ in range(t):
    # n = int(input())
    a,x,b,y = [int(i) for i in input().split()]
    alice = a/x
    bob = b/y
    if alice>bob:
        print("ALICE")
    elif bob>alice:
        print("BOB")
    else:
        print("EQUAL")
