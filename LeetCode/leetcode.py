from math import fabs


class Solution:
    def digArtifacts(self, n: int, artifacts: list[list[int]], dig: list[list[int]]) -> int:
        ans = 0
        for artifact in artifacts:
            a_stat = True
            for i in range(artifact[0], artifact[2] + 1):
                for j in range(artifact[1], artifact[3] + 1):
                    if [i, j] not in dig:
                        a_stat = False
                        break

                if not a_stat:
                    break
            if a_stat:
                ans+=1
        return ans




a = Solution()
print(a.digArtifacts(n=2, artifacts=[[0, 0, 0, 0], [0, 1, 1, 1]], dig=[[0, 0], [0, 1], [1, 1]]))
