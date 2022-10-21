def fact(k):
    if k <= 1:
        return 1
    else:
        return k * fact(k - 1)


class Solution:
    def findRank(self, S):
        # Code here
        s = S.lower()
        lessright = []
        ans = 0
        l = len(s)
        for i in range(l):
            lessright = [0] + lessright
            temp = s[i]
            for j in range(i + 1, l):
                if temp > s[j]:
                    lessright[0] += 1

        for k in range(l):
            ans += lessright[k] * fact(k)
        return ans + 1


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str1 = input().strip()
        obj = Solution()
        ans = obj.findRank(str1)
        print(ans)
