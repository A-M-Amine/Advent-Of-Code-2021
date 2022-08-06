def dynamic_fuel(f1,f2):
    
    dfuel = 0
    cpt = 1
    for i in range(min(f1,f2),max(f1,f2)):
        dfuel +=  cpt
        cpt += 1
    
    return dfuel

def C2(d):
    # binomial coefficient (d+1 choose 2)
    # 1+2+3+...+d ~ d**2. d terms, which average (d+1)/2.
    return d*(d+1)/2

def align(inpt):

    dicNb = {}
    for i in inpt:
        dicNb[i] = dicNb.get(i,0) + 1
    
    fuel = 0

    test = 0
 
    for k in dicNb.keys():

        som = 0
        for key, val in dicNb.items():

            if key != k:
                numb= abs(key-k)        #---- p1
                som += C2(numb) * val
                # if fuel == 206:
                #     test += 1
                #     print(k,val,dynamic_fuel(key,k))
                    
        
        # if test == 2:
        #     break

        if fuel == 0:
            fuel = som
        else:
            if som < fuel:
                fuel = som
        #print(fuel)
    
    return fuel



inpt = list(map(int,open('input7.txt').readline().split(",")))
print(align(inpt))
