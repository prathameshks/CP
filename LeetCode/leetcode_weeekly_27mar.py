class Solution:
    def makeone(self,nums):
        nl = nums[:]
        ans, l = 0, len(nums)
        for i in range(0, l, 2):
            if i + 1 < len(nl):
                if nl[i] == nl[i + 1]:
                    print(nl.pop(i), i)
                    ans += 1
            else:
                break
        if len(nl) % 2 != 0:
            ans += 1

        return ans

    def minDeletion(self, nums: list[int]) -> int:


ob=Solution().minDeletion([0,1,5,4,2,4,7,2,3,0,3,0,0,9,7,5,9,4,3,9,9,2,1,6,3,1,0,7,6,6,6,0,1,7,1,9,4,9,3,3,4,5,0,3,8,7,1,8,4,5])
print(ob)