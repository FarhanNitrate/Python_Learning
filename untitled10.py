st = input("enter a string: ")

def check_string(str1):
    for i in str1:
        if i == i.upper():
            return("True")
            break
        else:
            return("false")

x = check_string(st)
    
print(x)   
    
    
        
    
