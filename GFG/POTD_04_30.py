# User function Template for python3

class Solution:
    def SolveQueris(self, str1, Query):
        ans=[]
        for s,e in Query:
            ans.append(len(set(str1[s-1:e])))
        return ans



# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str = input()
        q = int(input())
        Query = []
        for i in range(q):
            a = list(map(int, input().split()))
            Query.append(a)
        obj = Solution()
        ans = obj.SolveQueris(str, Query)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends