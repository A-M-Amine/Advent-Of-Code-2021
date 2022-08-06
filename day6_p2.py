def emptydic(dic):
    for i in range(9):
        if i not in dic:
            dic[i] = 0

def bd_dic(dic):
    
    nb = 0
    print("val ",dic[0])
    for i in range(dic[0]):
        nb += 1

    return nb

def sub_dic(dic):

    for k, v in dic.items():
        if k == 0:
            dic[6] += 1
            dic[k] -= 1
        else:
            if v != 0:
                dic[k-1] += 1
                dic[k] -= 1


def p2(inpt,n):

    dic = {}
    emptydic(dic)
    for i in inpt:
        dic[i] += 1
    
    print(dic)
    for i in range(n):

        nb = bd_dic(dic)
        sub_dic(dic)
        dic[8] += nb

    print(dic)

    print(sum(dic.values()))
        
    
    # return res

def test(inpt,n):
    dic = {}
    tmp = {}
    
    emptydic(dic)
    for i in inpt:
        dic[i] += 1

    X = dic
    for i in range(n):

        emptydic(tmp)
        for x,cnt in X.items():
            if x==0:
                tmp[6] += cnt
                tmp[8] += cnt
            else:
                tmp[x-1] += cnt
        X = tmp
    

    print(sum(X.values()))

inpt = list(map(int,open('test.txt').readline().split(",")))

test(inpt,2)
# print(p2(inpt,1))