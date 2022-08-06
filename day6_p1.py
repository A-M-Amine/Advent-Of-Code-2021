def p1(inpt,n):
    
    for i in range(n):
        add = [8 for i in inpt if i == 0]
        tmp = list(map(lambda x: x-1 if x>0 else 6, inpt))
        tmp.extend(add)
        inpt = tmp[:]
    
    return len(inpt)
        
def p2(inpt):
    l = len(inpt)
    prc = 100 * (p1(inpt,2) - l) / l
    print(prc)
    res = l * (1 + prc)** 8

    return res

inpt = list(map(int,open('test.txt').readline().split(",")))



print(p1(inpt,32))
print(p2(inpt))