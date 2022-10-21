# User function Template for python3
from bisect import bisect_right

def greaterElement(arr, n):
    # Complete the function
    s = sorted(arr[:])
    ans = []
    for i in arr:
        j = bisect_right(s,i)
        if j == n:
            ans.append(-10000000)
        else:
            ans.append(s[j])

    return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

for _ in range(0, int(input())):

    n = int(input())
    arr = list(map(int, input().strip().split()))
    res = greaterElement(arr, n);
    ans = ""
    for i in res:
        if (i == -10000000):
            ans += "_ "
        else:
            ans += str(i) + " "
    print(ans)

# } Driver Code Ends