# Specifically, the H-index score of a researcher is the largest integer H such that the researcher has H papers with at least H citations each.
def findcan(num, arr, oldhi):
    c = 0
    for j in arr:
        if j >= num:
            c += 1
    print((num, arr, oldhi),c)
    return max(c, oldhi)


def find_citations(arr):
    hi = 0

    for j in range(len(arr)):
        hi = findcan(j + 1, arr, hi)

    return hi


def h_index(n, citations):
    ans = []
    for i in range(len(citations)):
        arr = citations[:i + 1]
        # print(arr)
        l=len(arr)
        hi=0
        for j in range(1,l+1):
            hi=findcan(j,arr,hi)
        # ans.append(find_citations(arr))

    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())  # The number of papers
        citations = list(map(int, input().split()))  # The number of citations for each paper
        h_index_scores = h_index(n, citations)
        # print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))
