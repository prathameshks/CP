# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())

for _ in range(t):
    n= input().strip()
    ans = True
    signc = 0
    for i in n:
        if i in '+-':
            signc+=1
        if not (i.isnumeric() or i in '.+-'):
            ans = False
            break
    if ans:
        if n.count('.')!=1 or signc>1:
            print(False)
        else:
            if signc == 1:
                num = n[1:]
            else:
                num = n
            if num.endswith('.'):
                print(False)
            else:
                print(True)
    else:
        print(False)


"""
+4.50
-1.0
.5
-.7
+.4
 -+4.5
 12.
12.0   
"""