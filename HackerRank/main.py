def average(array):
    arr = set(array)
    # your code goes here
    avg = sum(arr) / len(arr)
    return round(avg,3)
def solve(s):
    a=''
    for char in range(len(s)):
        if char-1 >=0:
            if s[char-1]==' ':
                a+=s[char].upper()
            else:
                a+=s[char].lower()
        else:
            a += s[char].upper()
    return a

if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().split()))
    # result = average(arr)
    print(solve('hello  world lol'))