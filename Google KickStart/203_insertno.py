t = int(input())
for case_no in range(1, t + 1):
    ques =n= int(input())
    s = 0
    while n!=0:
        s+=n%10
        n//=10
    if s%9 !=0:
        need = 9 - (s % 9)
    else:
        need=0
    ans=str(ques)
    for i in range(len(ans)):
        if int(ans[i])>need:
            ans = ans[:i]+str(need)+ans[i:]
            break
    print("Case #{}: {}".format(case_no, int(ans)))
