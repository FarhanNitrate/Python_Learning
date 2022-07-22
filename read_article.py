
def read_doc(st1):
    
    file = open(st1,'r')
    data = file.read()
    
    my_dict = {}
    
    sp = data.split()
    
    for i in sp:
        if i in my_dict:
            my_dict[i] += 1
        
        else:
            my_dict[i] = 1
    
    s_d = open("new.txt","w")
        
    for k, v in my_dict.items():
        print(k+" "+str(v))
        
        
        s_d.write(k+" "+str(v))
        
       
        
    s_d.close()
        
        
        
    
    
        

        
        # stored_data = open("student.txt","w")
        # data = stored_data.write()
        
        
    
    # stored_data = open("demo.txt","w")
    # data = stored_data.write(my_dict)
    # print(data)
read_doc("article.txt")

