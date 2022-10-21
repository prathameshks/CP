t = int(input())


def checkin(n):
    p = 1
    s = 0
    while n != 0:
        f = (n % 10)
        p *= f
        s += f
        n = n // 10

    if p % s == 0:
        return True
    else:
        return False


for case_no in range(1, t + 1):
    A, B = [int(a) for a in input().split()]

    ans = 0
    for j in range(A, B + 1):
        if checkin(j):
            ans += 1

    print("Case #{}: {}".format(case_no, ans))
