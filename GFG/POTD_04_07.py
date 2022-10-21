#User function Template for python3

class Solution:
    def LCP(self,arr,n):
        l = sorted(arr)
        ans = ''
        for i in range(min(len(l[0]), len(l[-1]))):
            if l[0][i] == l[-1][i]:
                ans += l[0][i]
        if ans == '':
            return -1
        else:
            return ans

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs =int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[ x  for x in input().split()]
        obj=Solution()
        print(obj.LCP(arr,n))
# } Driver Code Ends