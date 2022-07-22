st = input("ENTER A STRING: ")

def chk_st(x):
    #return sum(map(ord,x))
    total = 0
    for i in range(0,len(x)):
        ad = ord(st[i])
        total = total + ad
    x = print(total)
    return(x)

chk_st(st)       