def timeConversion(s):
    # Write your code here
    mer = s[-2:]
    print(s[-2])
    hr, mn, sc = s[:-2].split(':')
    if mer == 'AM':
        if hr != '12':
            return s[-2]
        else:
            return ':'.join(['00', mn, sc])
    else:
        if hr == '12':
            return s[-2]
        else:
            ans = (int(hr) + 12)
            return ':'.join([str(ans), mn, sc])

print(timeConversion(input()))