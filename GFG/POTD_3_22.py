import bisect


def Smallestonleft(arr, n):
    # Complete the function
    ans = []
    arr1 = []
    for i in range(n):
        bisect.insort(arr1, arr[i])
        k = bisect.bisect_left(arr1, arr[i])
        if k == 0:
            ans.append(-1)
        else:
            ans.append(arr1[k - 1])

    return ans

s=Smallestonleft([2, 3, 4, 5, 1],5)
print(s)