# User function Template for python3


def calculate(arr, n):
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]^arr[j] == 0:
                ans+=1
    return ans

# {
#  Driver Code Starts
# Initial Template for Python 3

for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    res = calculate(arr, n)
    print(res)

# } Driver Code Ends