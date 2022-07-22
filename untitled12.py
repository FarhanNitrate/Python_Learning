user = input("enter username: ")
password = input("enter password: ")
def mixstr(username , password):
    st1 = user[0:4] + password[-4:]
    print(st1)

mixstr(user , password)