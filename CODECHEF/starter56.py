t = int(input())

for i in range(t):
    col = [int(i) for i in input().split()]
    # n = int(input())
    # s = input()
    r,g,b = col[0],col[1],col[2]
    for i in range(3):
        if i>3:
            col[i] = 3
    col = set(col)
    
    if col == {2,3,3}:
        print(5)
    else:
        r,g,b = [int(i) for i in input().split()]
        # n = int(input())
        # s = input()
        ans = 0
        if r>=1:
            ans+=1
            r-=1
        if g>=1:
            ans+=1
            g-=1
        if b>=1:
            ans+=1
            b-=1
        if r>=1 and g>=1:
            ans += 1
            r-=1
            g-=1
        if r>=1 and b>=1:
            ans += 1
            r-=1
            b-=1
        if b>=1 and g>=1:
            ans += 1
            b-=1
            g-=1
        # print(" * ",end='')
        print(ans)

'''
000
001
011
111
200
210
211
221
222
223
233
'''


exit()
t = int(input())

for i in range(t):
    r,g,b = [int(i) for i in input().split()]
    # n = int(input())
    # s = input()
    ans = 0
    if r>=1:
        ans+=1
        r-=1
    if g>=1:
        ans+=1
        g-=1
    if b>=1:
        ans+=1
        b-=1
    if r>=1 and g>=1:
        ans += 1
        r-=1
        g-=1
    if r>=1 and b>=1:
        ans += 1
        r-=1
        b-=1
    if b>=1 and g>=1:
        ans += 1
        b-=1
        g-=1
    # print(" * ",end='')
    print(ans)




t = int(input())

for i in range(t):
    n,m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    # n = int(input())
    # s = input()
    mid = (m+1)/2
    d=0
    for i in a:
        if i>mid:
            d+=(i-1)
        else:
            d+=(m-i)
    # print(" * ",end='')
    print(d)

    
'''
1-10 mid = 5.5
5 10 = 5
   1 = 4
6 10 = 4
   1 = 5
1-11 mid = 6
5 1= 4
11 = 6
6 1 =5
11 = 5

'''