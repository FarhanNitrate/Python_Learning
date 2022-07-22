n = int(input("enter number whose table to match: "))
d = input("enter doc to match with: ")
lst = []
lst2 = []

def match_table(n,doc):
    file = open(doc,'r')
    for i in range(1,11):
        z = str(n*i)
        lst.append(z)


    data = file.read()
    lst2 = data.split()


    if lst == lst2:
        print("True")
    else:
        print("false")

match_table(n,d)
    

    
    
    
    
    