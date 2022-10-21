
from itertools import count


slab = [0,250000, 250000, 500000, 750000, 1000000, 1250000, 1500000]
percnt = [0,0, 5, 10, 15, 20, 25, 30]

for _ in range(int(input())):
    # n,m = [int(x) for x in input().split()]
    amt = n = int(input())
    tax = 0
    count = 0
    per = 0
    while(n>250000):
        count+=1
        if(count<7):
            tax+=2500*per
            n-=250000
            per+=5
        else:
            break
    tax+=( n *per/100)
    print(int(amt-tax))
exit()
for _ in range(int(input())):
    # n,m = [int(x) for x in input().split()]
    amt = n = int(input())
    ans=0
    cur = 1
    while n>slab[cur]:
        if n>slab[cur+1]:
            ans+=(slab[cur]-slab[cur-1])*percnt[cur]/100
            print(cur,ans)
        cur+=1
    ans+=(n-slab[cur-1])*percnt[cur]/100

    print(cur,ans)
    # print(cur)
    # for i in range(cur-1,-1,-1):
    #     ans+=slab[i]*percnt[i]/100

    print(amt - int(ans))

exit()
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    severity = 0
    ans = "FINE"
    for i in range(n):
        sol, cases = input().split()
        if (sol == "correct" and '0' in cases and severity < 2):
            ans = "INVALID"
            severity = 2
            # break
        if sol == "wrong":
            if ('0' not in cases and severity != 2):
                ans = "WEAK"
                severity = 1
                # break
    print(ans)
