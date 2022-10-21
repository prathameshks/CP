t = int(input())

for i in range(t):
    a,b = input().split()
    ab = set(a+b)
    # num = [int(i) for i in input().split()]
    child = []
    n = int(input())
    for j in range(n):
        child.extend(list(input()))
    ans = 'YES'
    for x in list(set(child)):
        if x not in ab:
            ans = 'NO'
            break
    print(ans)
