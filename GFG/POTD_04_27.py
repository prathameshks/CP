#User function Template for python3

class Solution1:
    def killinSpree (self, n):
        # code here
        # s=n(n+1)(2n+1)/6
        # end=False
        p=1
        while True:
            n-=p*p
            if n==0:
                return p
            elif n<0:
                return p-1
            else:
                p+=1

class Solution:
    def killinSpree (self, n):
        # code here
        low =1
        high = 14422
        while low<=high:
            mid = (low+high) //2
            val = mid*(mid+1)*(2*mid+1)/6
            if val < n:
                low = mid+1
                ans = mid
            elif val>n:
                high = mid-1
            else:
                ans = mid
                break
        return ans

#{14421
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.killinSpree(N);
        print(ans)




# } Driver Code Ends