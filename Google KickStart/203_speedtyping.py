t = int(input())
for case_no in range(1, t + 1):
    ques = list(input())
    typed = list(input())
    l = len(ques)
    t = len(typed)
    if l >= t and ques != typed:
        print("Case #{}: {}".format(case_no, 'IMPOSSIBLE'))
        continue
    mis = 0
    for char in range(l):
        if mis == "IMPOSSIBLE":
            break
        while ques[char] != typed[char]:
            typed.pop(char)
            mis += 1
            if mis + char > len(typed):
                mis = 'IMPOSSIBLE'
                break
    if mis == 0 and l < t:
        mis = t - l

    print("Case #{}: {}".format(case_no, mis))









"""l = len(ques)
    mis = 0
    for char in range(l):
        if mis == "IMPOSSIBLE":
            break
        if ques[char] == typed[char + mis]:
            pass
        else:
            while ques[char] != typed[char + mis]:
                mis += 1
                if char + mis >= l:
                    mis = "IMPOSSIBLE"
                    break
    print("Case #{}: {}".format(case_no, mis))
"""
