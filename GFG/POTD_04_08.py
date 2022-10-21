import collections


class Solution:
    def print_next_greater_freq(self, arr, n):
        cnt = collections.Counter(arr)
        new = [cnt[i] for i in arr]
        ans = []
        for j in range(n):
            for x in range(j + 1,n):
                if (new[x] > new[j]) and (arr[j] != arr[x]):
                    ans.append(arr[x])
                    break
            else:
                ans.append(-1)
        return ans


# code here


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        ans = obj.print_next_greater_freq(arr, n)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends
