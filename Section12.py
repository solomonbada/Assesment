with open('users.txt', 'a+') as u:
    user_fname = input("Please Enter Your First Name: ")
    user_sname = input("Please Enter Your Second Name: ")
    user_add1 = input("Please Enter Your First Line Of Address: ")
    user_add2 = input("Please Enter Your City: ")
    user_postcode = input("Please Enter Your Post Code: ")
    user_number = input("Please Enter Your Telephone Number: ")

    #u.readline()
    ID_Counter = 4
    u.write('\n')
    u.write(str(ID_Counter))
    u.write('\n')
    u.write(user_fname.capitalize())
    u.write('\n')
    u.write(user_sname.capitalize())
    u.write('\n')
    u.write(user_add1.capitalize())
    u.write('\n')
    u.write(user_add2.capitalize())
    u.write('\n')
    u.write(user_postcode.upper())
    u.write('\n')
    u.write(user_number)
    ID_Counter =+ 1

u.close()