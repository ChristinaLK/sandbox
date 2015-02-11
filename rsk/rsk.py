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

perm = sys.argv[1:]
##note that input needs to be numbers separated by SPACES

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
            
print tableaux
