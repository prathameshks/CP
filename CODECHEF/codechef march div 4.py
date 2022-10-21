# 6
t = int(input())

for _ in range(t):
    n,x=[int(a) for a in input().split()]
    c,i,u = 0,0,0
    c+=x//3
    xr=x%3
    if xr != 0:
        c+=1 #10
        i+=3-xr #1
    u=n-c-i #10-10-1 == -1
    if u<=n and u>=0:
        print('YES')
        print(c,i,u)
    else:
        print("NO")


exit()
# 4
t = int(input())

for _ in range(t):
    n = int(input())
    if n%2==0:
        print(n//2)
    else:
        print((n//2)+1)




# 1
t = int(input())

for _ in range(t):
    throw=[int(a) for a in input().split()]
    print(max(throw))


# 3
t = int(input())

for _ in range(t):
    s,t = input(),input()
    m=''
    for i in range(5):
        if s[i]==t[i]:
            m+='G'
        else:
            m+='B'
    print(m)

# 2
t = int(input())

for _ in range(t):
    x,y=[int(a) for a in input().split()]
    min_w = 2*y
    print(x//min_w)