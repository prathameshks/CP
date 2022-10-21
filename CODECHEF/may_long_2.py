# div 4

# 5

t = int(input())

for _ in range(t):
    # x, y = [int(i) for i in input().split()]
    n = int(input())
    s = input()
    c0,c1 = 0,0
    for i in range(0,(n//2)+1):
        if s[i] != s[n-i-1]:
            if s[i]=='0':
                c0+=1
            else:
                c1+=1
    ans = c0//2 + c0%2 + c1//2 + c1%2
    print(ans)

'''
# 4

t = int(input())

for _ in range(t):
    # x, y = [int(i) for i in input().split()]
    n = int(input())
    s = [int(i) for i in input().split()]
    for i in range(n-1,-1,-1):
        if s[i]!=0:
            print(i)
            break

# 3

t = int(input())

for _ in range(t):
    # x, y = [int(i) for i in input().split()]
    n = int(input())
    s = [int(i) for i in input().split()]
    print(max(s))



#2

p = [int(i) for i in input().split()]
# n = int(input())
# s = [int(i) for i in input().split()]
ans=0
for i in p:
    if i>=10:
        ans+=1
print(ans)

#1

t = int(input())

for i in range(t):
    x, y = [int(i) for i in input().split()]
    # n = int(input())
    # s = [int(i) for i in input().split()]
    print(int(x*10 + y*90))
'''