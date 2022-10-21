def find_ans(n, a):
    diff = []
    zero = 0
    for j in range(0, n//2):
        val = a[n-j-1]-a[j]
        if val < 0:
            print(-1)
            return
        elif val == 0:
            zero += 1
        diff.append(val)
    if zero == n//2:
        print(0)
        return
    for elmt in range(n//2-1):
        if diff[elmt] < diff[elmt+1]:
            print(-1)
            return
    print(diff[0])


for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    find_ans(n, a)
