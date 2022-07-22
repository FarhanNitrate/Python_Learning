st = input("Enter a word: ")
st1 = st.lower()
my_dict = {}
for i in st1:
    if i in my_dict:
        my_dict[i] += 1
        
    else:
        my_dict[i] = 1
    
    
        
map_ = print(my_dict)
print(map_)
    