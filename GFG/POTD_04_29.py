# User function Template for python3

class Solution:

    def candyStore(self, candies, N, K):
        # code here
        candy1 = candies[:]
        candy2 = candies[:]
        a1 = a2 = 0
        while candy1 != []:
            a1 += min(candy1)
            candy1.remove(min(candy1))
            for x in range(min(K, len(candy1))):
                candy1.remove(max(candy1))
        while candy2 != []:
            a2 += max(candy2)
            candy2.remove(max(candy2))
            for y in range(min(K, len(candy2))):
                candy2.remove(min(candy2))
        return [a1, a2]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N, K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies, N, K))
# } Driver Code Ends
