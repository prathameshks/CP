# User function Template for python3

def isValid(s):
    ip = s.split('.')
    if len(ip) != 4 or '' in ip:
        return 0
    for i in ip:
        if (i!='0' and i[0]=='0') or not(i.isnumeric()):
            return 0
        elif not (int(i) <=255 and int(i) >= 0):
            return 0
    return 1

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        if (isValid(s)):
            print(1)
        else:
            print(0)

# } Driver Code Ends