# User function Template for python3

class Solution:
    def reArrange(self, arr, N):
        # code here
        even = []
        odd = []
        for i in range(N):
            if i % 2 == 0:
                if arr[i] % 2 != 0:
                    if odd == []:
                        even.append(i)
                    else:
                        arr[odd[0]], arr[i] = arr[i], arr[odd[0]]
                        odd.pop(0)
            else:
                if arr[i] % 2 == 0:
                    if even == []:
                        odd.append(i)
                    else:
                        arr[even[0]], arr[i] = arr[i], arr[even[0]]
                        even.pop(0)
        # print(arr)
        return arr

# {
#  Driver Code Starts
# Initial Template for Python 3


def check(arr, n):
    flag = 1
    c = d = 0
    for i in range(n):
        if i % 2 == 0:
            if arr[i] % 2:
                flag = 0
                break
            else:
                c += 1
        else:
            if arr[i] % 2 == 0:
                flag = 0
                break
            else:
                d += 1
    if c != d:
        flag = 0

    return flag


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ob.reArrange(arr, N)

        print(check(arr, N))

# } Driver Code Ends
