# User function Template for python3

class Solution:
    def swapBits(self, X, P1, P2, N):
        b= bin(X)[2:]
        b='0'*(2*N+P1+P2-len(b)) + b
        if P1 == 0:
            s1=''
            s2 = b[-P1-N:]
        else:
            s1 = b[-P1:]
            s2 = b[-P1-N:-P1]
        s3 = b[-P2:-P1-N]
        s4 = b[-P2-N:-P2]
        s5 = b[:-P2-N]
        print(s5,s4,s3,s2,s1,'-',b)
        return int(s5+s2+s3+s4+s1,2)


# {
#  Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        obj = Solution()
        X, P1, P2, N = map(int, input().split())
        print(obj.swapBits(X, P1, P2, N))

# } Driver Code Ends
