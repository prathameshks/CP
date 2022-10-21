# 'a' = 96+1
def print_rangoli(size):
    s = ((size - 1) * 4) + 1
    for line in range(1,size+1):
        str1 = str2 = ''
        for i in range(size,size-line,-1):
            str1 += chr(96+i)
        for j in range(size-line+2,size+1):
            str2 += chr(96+j)
        mainstr = str1+str2
        print(('-'.join(mainstr)).center(s,'-'))
    for line in range(size-1,0,-1):
        str1 = str2 = ''
        for i in range(size,size-line,-1):
            str1 += chr(96+i)
        for j in range(size-line+2,size+1):
            str2 += chr(96+j)
        mainstr = str1+str2
        print(('-'.join(mainstr)).center(s,'-'))
print_rangoli(int(input('Size(1 to 26):')))
a=input()