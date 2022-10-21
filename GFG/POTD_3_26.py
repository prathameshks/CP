# User function Template for python3

class Solution:
    def findMaxAverage(self, arr, n, k):
        sumarr = [0]
        for x in range(0, k):
            sumarr[0] += arr[x]
        for i in range(1, n):
            if i + k <= n:
                sumarr.append(sumarr[i - 1] - arr[i - 1] + arr[i + k-1])
        return sumarr.index(max(sumarr))



# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxAverage(arr, n, k)
        for i in range(ans, ans + k):
            print(arr[i], end=" ")
        print()
        tc -= 1
# } Driver Code Ends
