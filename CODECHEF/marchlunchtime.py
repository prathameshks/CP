t=int(input())

def even(a):
    if int(a)%2==0:
        return True
for i in range(t):
    # n,x=[int(i) for i in input().split()]
    n=input()
    e=z=o=0
    for i in n:
        if i=='0':
            z+=1
        elif even(i):
            e+=1
        else:
            o+=1
    if e>=2 or o>=2:
        print("YES")
    
    elif (z>=2 and e+o>=2):
        print("YES")
        
    else:
        print("NO")