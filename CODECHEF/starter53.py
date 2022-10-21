# chess
def printchess(king,queen):
    chess = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    chess[king[0]-1][king[1]-1] = 1
    for coords in queen:
        chess[coords[0]-1][coords[1]-1] = 2
    for i in chess:
        for j in i:
            print(j,end=" ")
        print()

lst = [3,1,2,5,5]
val = []
fqy = []
for i in lst:
    if i in val:
        fqy[val.index(i)] += 1 
    else:
        val.append(i)
        fqy.append(1)
# print(val)
# print(fqy)

m = 0
for i in fqy:
    if i>m:
        m=i

for i in range(len(fqy)):
    if fqy[i] == m:
        ind = i
        break

print("Mark with highest frequency is ",val[ind])