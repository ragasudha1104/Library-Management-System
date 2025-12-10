rom assets.data import LMS

def check_name_password(credentials):
    admin = credentials[0]
    name = credentials[1]
    password = credentials[2]
    if (admin["name"] == name) and (admin["password"] == password):
        return True
    else:
        return False
def login():
    name = input("Please enter your name:")
    password = input("Please enter your password:")
    # status = False
    # for admin in LMS["ADMINS"]:
    #     if (admin["name"] == name) and (admin["password"] == password):
    #         status = True
    #         break
    
    # if status:
    #     print("Login is Successfull.")
    # else:
    #     print("Login is unsuccessfull.")

    ### updated version
    all_admins = list(zip(LMS["ADMINS"],[name]*len(LMS["ADMINS"]),\
                          [password]*len(LMS["ADMINS"])))
    output = list(filter(check_name_password,all_admins))
    
    if output:
        status = True
    else:
        status = False
    return status        