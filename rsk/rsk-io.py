#!/c/Anaconda/python
import sys

def lineTest(tabl,ind,num):
    switch = True
    for i in tabl[ind]:
        if i > num:
            switch = False
            break
    return switch

def RSKappend(tabl, num, ind):
    tabl[ind].append(num)
    return False

def RSKreplace(tabl, num, ind):
    retVar = 0
    for i in tabl[ind]:
        if i > num:
            tabl[ind][tabl[ind].index(i)] = num
            retVar = i
            break
    return retVar

def RSKprint(tabl):
    for row in tabl:
        print row

##producing tableau

script = sys.argv[0]
filename = sys.argv[1]

#perm = sys.argv[1:]
##note that input needs to be numbers separated by SPACES

file = open(filename)
perm = file.readline().split()
perm = [int(x) for x in perm]

tableaux = [[]]

for j in perm:
    bln = True
    index = 0
    while bln:
        if len(tableaux) <= index:
            tableaux.append([])
        if lineTest(tableaux, index, j):
            bln = RSKappend(tableaux, j, index)
        else:
            j = RSKreplace(tableaux, j, index)
            index += 1
            
#RSKprint(tableaux)

tableaux = str(tableaux)

out_file = open('output.txt', 'w')
out_file.write(tableaux)
