
lst = open("input2.txt").readlines()

hpos = 0
depth = 0
aim = 0

for i in lst:
    if i[0] == 'f':
        hpos += int(i.split(" ")[1])
        depth += aim * int(i.split(" ")[1])
    if i[0] == 'u':
        aim -= int(i.split(" ")[1])
    if i[0] == 'd':
        aim += int(i.split(" ")[1])

print(depth)
print(hpos)

print(depth*hpos)
