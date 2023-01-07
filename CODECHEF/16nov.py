# Click on the SUBMIT button to solve your first problem on CodeChef.


t=int(input())
for i in range(t):
    # X,Y=map(int,input().split())
    x,y = [int(a) for a in input().split()]
    print(max(x,y))
    # x,y = int(input())