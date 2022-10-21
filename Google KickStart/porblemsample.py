t = int(input())
for case_no in range(t):
    n, m = [int(a) for a in input().split()]
    bag = [int(a) for a in input().split()]
    rem = sum(bag) % m
    print("Case #{}: {}".format(case_no, rem))
