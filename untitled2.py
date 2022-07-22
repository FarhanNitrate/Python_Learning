



def read_doc(st1):
    
    file = open(st1,'r')
    data = file.readlines()
    map_ = {}


    for i in data:
        sub, nam = i.split()
        if sub in map_:
            map_[sub].add(nam)
        else:
            map_[sub] = {nam}
    file.close()
    return map_
            
map_ = read_doc("student.txt")  
print(map_)

