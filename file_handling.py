# file = open('demo.txt', 'r')
# # data = file.read()
# data = file.readlines()
# print(data)

# file = open("demo.txt",'w')
# file.write("this is a demo text")
# file.writelines([
#     'this is demo 2',
#     "this is demo 3"
#     ])
# file.close()

file = open("demo.txt",'a')
file.write("this is a demo text love")

file.close()

file = open('demo.txt', 'r')
data = file.read()

print(data)