# 6

t = int(input())

for _ in range(t):
    n=int(input())
    s=input()
    ans=0
    for i in range(n,0,-1):
        sn=s[:i+1]
        tans = ''
        l=i
        for j in range(i):
            print(sn,i-j)
            tans = str(int(sn[i-j])*(l%2)) + tans
            l-=1
        ans^=int(tans,2)
    print(ans)

exit()
# n,x=[int(a) for a in input().split()]




# 6
t = int(input())

for _ in range(t):
    n=int(input())
    s=input()
    ans=0
    for char in range(n-1,-1,-1):
        for i in range(char+1):
            ans^=int(s[i:char+1],2)
    print(ans)






# 5
t = int(input())

def len_list(l):
    ans =[]
    for i in l:
        ans.append(len(i))
    return ans
for _ in range(t):
    s=input()
    px,sx=s[0],s[-1]
    subs = []
    a=s.split(px)
    for i in a:
        subs.extend(i.split(sx))
    lens = len_list(subs)
    m = max(lens)
    if m==0:
        print(-1)
    else:
        print(m)







# 4
t = int(input())

for _ in range(t):
    n,x=[int(a) for a in input().split()]
    c,i,u = 0,0,0
    c+=x//3
    xr=x%3
    if xr>0:
        c+=1
        i+=3-xr
    u=n-c-i
    if u<=n and u>=0:
        print('YES')
        print(c,i,u)
    else:
        print("NO")





# 3
t = int(input())

for _ in range(t):
    n=int(input())
    if n%2==0:
        print(n//2)
    else:
        print((n+1)//2)





# 2
t = int(input())

for _ in range(t):
    n=int(input())
    ans=0
    if n-6>=0:
        ans+=1
        n-=6
        ans+= n//7

    print(ans)
    



#1

t = int(input())

for _ in range(t):
    s,t=input(),input()
    ans=''
    for i in range(5):
        if s[i]==t[i]:
            ans+='G'
        else:
            ans+='B'
    print(ans)
    