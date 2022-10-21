# cook your dish here
for _ in range(int(input())):
    n,k =  [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    prot = 0
    flag=0
    for i in range(n):
        if(prot+a[i])<k:
            print("NO",i+1)
            flag =1
            break
        else:
            prot = prot+a[i]-k
    if flag==0:
        print("YES")