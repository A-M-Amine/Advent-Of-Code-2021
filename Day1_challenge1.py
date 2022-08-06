

 
lst = [int(i.strip("\n")) for i in open("input.txt").readlines()]

count = 0
sumx = lst[0] + lst[1] + lst[2]
for i in range(1,len(lst)-2):
    sumy = lst[i] + lst[i+1] + lst[i+2]
    if sumy > sumx:
        count += 1
    sumx = sumy

print(count)


