t = int(input())

for i in range(t):
    # num = [int(i) for i in input().split()]
    n = int(input())
    ans = 0
    cur = 1
    while cur < n:
        ans += (n - cur + 1) ** 2
        cur += 2
    if n%2 == 0:
        print(ans)
    else:
        print(ans+1)