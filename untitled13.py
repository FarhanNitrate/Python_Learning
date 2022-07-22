#97 to 122
st3 = input("enter string: ")
def chk(st3):
    count = 0
    for i in range(0,(len(st3)-1)):
        # for j in range(1,len(st3)):
            if (ord(st3[i])+1) == ord(st3[i+1]):
                count += 1
            
            else:
                count += 0
    print(count)
            

chk(st3)
        
        