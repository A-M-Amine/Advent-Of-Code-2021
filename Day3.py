

from typing import List


lst = open("input3.txt").readlines()
lst = [i.strip("\n") for i in lst]

gamma = ""
ep = ""
l = len((lst[0]))
for i in range(len(lst[0])):
    nb1 = 0
    for j in lst:
        if j[i] == '1':
            nb1 += 1
    if nb1 > len(lst) - nb1:
        gamma += '1'
    else:
        gamma += '0'



print(int(gamma,2))

for i in gamma:
    if i == '0':
        ep += '1'
    else:
        ep += '0'


print(int(ep,2))

print(int(gamma,2)*int(ep,2))
    

