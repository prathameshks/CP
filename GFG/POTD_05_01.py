# User function Template for python3
def is_prime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


def prime_up_to(n):
    primes = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    prm = []
    for p in range(2, n + 1):
        if primes[p]:
            prm.append(p)
    return prm


class Solution:
    def superPrimes(self, n):
        primes = prime_up_to(n)
        ans = 0
        for i in primes:
            if i - 2 in primes:
                ans += 1
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.superPrimes(n)
        print(ans)

# } Driver Code Ends
