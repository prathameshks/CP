
# for i in range(1,10001):
#     for j in range(1, 10001):
#         print(i,j,i+j,i-j,i*j,i//j,sep='--')
#
# exit()
t = int(input())

for i in range(t):
    num = [int(i) for i in input().split()]
    # s = int(input())
    nums = num[::]
    p = max(nums)
    nums.remove(p)
    a = max(nums)
    nums.remove(a)
    if p - a == 1:
        a, p = p, a

    d = a ** 2 - 4 * p
    if d >= 0:
        ans1a = int(a + d ** 0.5) / 2
        ans1b = int(a - d ** 0.5) / 2
        ans2a = int(p / ans1a)
        ans2b = int(p / ans1b)
        if ans1a > 0 and ans2a > 0:
            ans1, ans2 = ans1a, ans2a
            if ans1 + ans2 == a and ans1 - ans2 in nums and ans1 * ans2 == p and ans1 // ans2 in num:
                print(ans1, ans2)
            else:
                print(-1, -1)
        elif ans1b > 0 and ans2b > 0:
            ans1, ans2 = ans1b, ans2b
            if ans1 + ans2 == a and ans1 - ans2 in nums and ans1 * ans2 == p and ans1 // ans2 in num:
                print(ans1, ans2)
            else:
                print(-1, -1)
        else:
            print(-1, -1)

    else:
        print(-1, -1)
