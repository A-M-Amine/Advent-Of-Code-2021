

lst = open("input3.txt").readlines()
lst = [i.strip("\n") for i in lst]

gamma = ""
ep = ""

tmpo2 = []
tmpco2 = []

tmp1 = []
tmp0 = []

l = len((lst[0]))

tmpo2.extend(lst)

i = 0
while len(tmpo2)>1 and i < l:

    nb1 = 0
    tmp0.clear()
    tmp1.clear()
    for j in tmpo2:
        if j[i] == '1':
            nb1 += 1
            tmp1.append(j)
        else:
            tmp0.append(j)

    if nb1 >= len(tmpo2) - nb1:
        tmpo2.clear()
        tmpo2 = tmp1[:]     
    else:
        tmpo2.clear()
        tmpo2 = tmp0[:]
    
    i += 1


tmpco2.extend(lst)

i = 0
while len(tmpco2)>1 and i < l:

    nb1 = 0
    tmp0.clear()
    tmp1.clear()
    for j in tmpco2:
        if j[i] == '1':
            nb1 += 1
            tmp1.append(j)
        else:
            tmp0.append(j)

    if nb1 < len(tmpco2) - nb1:

        tmpco2.clear()
        tmpco2 = tmp1[:]     
    else:
        tmpco2.clear()
        tmpco2 = tmp0[:]
    
    i += 1



print(tmpco2[0])
print(int(tmpo2[0],2)*int(tmpco2[0],2))



    

