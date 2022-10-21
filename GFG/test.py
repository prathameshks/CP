
f=open('POTD_3_20.py','r')

import os


print(os.path.dirname('/POTD_3_20.py'))
print(os.path.basename('/POTD_3_20.py'))
print(os.path.relpath('/POTD_3_20.py'))
# os.path.abs('/POTD_3_20.py')

# os.path.relpath()
exit()
def a():
    x=9

print(a())
exit()
class demo():
    def __repr__(self):
        return '__repe py fun'

    def __str__(self):
        return 'str builtin fuk'


s = demo()
print(s)

exit()


# User function Template for python3

class Solution:
    def multiplyStrings(self, s1, s2):
        # code here
        a = int(s1) * int(s2)
        return int(a)
        # return the product string


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = input().split()
        print(Solution().multiplyStrings(a.strip(), b.strip()))

# } Driver Code Ends
