
lst = []


while True:
        op = input('enter operation string: ')
        op_list = op.split()
        print(op_list)
    
        if op_list[0] == "stop":
            break

        elif op_list[0] == 'push':
            lst.append(op_list[1])
            print(lst)
    
        elif op_list[0] == 'pop':
            lst.remove(op_list[1])
            
            
        
        
    
    