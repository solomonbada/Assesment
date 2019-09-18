#def update():


# with is like your try .. finally block in this case
with open('users.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

#print(data)
#print("Your name: " + data[2])

# now change the 2nd line, note that you have to add a newline
#data[1] = 'Solomon\n'

# and write everything back
#with open('users.txt', 'w') as file:
    #file.writelines( data )



def user1():
    if user_input2 == "FIRST NAME":
        print("Current: " + data[1])
        f_name_change = input("Please Enter New First Name: ")
        print("Updated: " + f_name_change)
        data[1] = (f_name_change + "\n")
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "SECOND NAME":
        print("Current: " + data[2])
        s_name_change = input("Please Enter New Second Name: ")
        print("Updated: " + s_name_change)
        data[2] = (s_name_change + "\n")
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "ADDRESS 1":
        print("Current: " + data[3])
        add_ = input("Please Enter New First Address: ")
        print("Updated: " + add_)
        data[3] = (add_ + "\n")
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "ADDRESS 2":
        print("Current: " + data[4])
        add2_ = input("Please Enter New Second Address: ")
        print("Updated: " + add2_)
        data[4] = (add2_ + "\n" )
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "POST CODE":
        print("Current: " + data[5])
        pcode = input("Please Enter New Post Code: ")
        print("Updated: " + pcode)
        data[5] = (pcode + "\n" )
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "TEL NUMBER":
        print("Current: " + data[6])
        tel = input("Please Enter New Tel Number: ")
        print("Updated: " + tel)
        data[6] = (tel + "\n" )
        with open('users.txt', 'w') as file:
            file.writelines(data)

#===========================================================================================

def user2():
    if user_input2 == "FIRST NAME":
        print("Current: " + data[8])
        f_name_change = input("Please Enter New First Name: ")
        print("Updated: " + f_name_change)
        data[8] = (f_name_change + "\n")
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "SECOND NAME":
        print("Current: " + data[9])
        s_name_change = input("Please Enter New Second Name: ")
        print("Updated: " + s_name_change)
        data[9] = (s_name_change + "\n")
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "ADDRESS 1":
        print("Current: " + data[10])
        add_ = input("Please Enter New First Address: ")
        print("Updated: " + add_)
        data[10] = (add_ + "\n")
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "ADDRESS 2":
        print("Current: " + data[11])
        add2_ = input("Please Enter New Second Address: ")
        print("Updated: " + add2_)
        data[11] = (add2_ + "\n" )
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "POST CODE":
        print("Current: " + data[12])
        pcode = input("Please Enter New Post Code: ")
        print("Updated: " + pcode)
        data[12] = (pcode + "\n" )
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "TEL NUMBER":
        print("Current: " + data[13])
        tel = input("Please Enter New Tel Number: ")
        print("Updated: " + tel)
        data[13] = (tel + "\n" )
        with open('users.txt', 'w') as file:
            file.writelines(data)




def user3():
    if user_input2 == "FIRST NAME":
        print("Current: " + data[15])
        f_name_change = input("Please Enter New First Name: ")
        print("Updated: " + f_name_change)
        data[15] = (f_name_change + "\n")
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "SECOND NAME":
        print("Current: " + data[16])
        s_name_change = input("Please Enter New Second Name: ")
        print("Updated: " + s_name_change)
        data[16] = (s_name_change + "\n")
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "ADDRESS 1":
        print("Current: " + data[17])
        add_ = input("Please Enter New First Address: ")
        print("Updated: " + add_)
        data[17] = (add_ + "\n")
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "ADDRESS 2":
        print("Current: " + data[18])
        add2_ = input("Please Enter New Second Address: ")
        print("Updated: " + add2_)
        data[18] = (add2_ + "\n" )
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "POST CODE":
        print("Current: " + data[19])
        pcode = input("Please Enter New Post Code: ")
        print("Updated: " + pcode)
        data[19] = (pcode + "\n" )
        with open('users.txt', 'w') as file:
            file.writelines(data)
    elif user_input2 == "TEL NUMBER":
        print("Current: " + data[20])
        tel = input("Please Enter New Tel Number: ")
        print("Updated: " + tel)
        data[20] = (tel + "\n" )
        with open('users.txt', 'w') as file:
            file.writelines(data)



user_input = input("Which ID Would You Like To Change?\n[1] [2] [3]: ")
user_input2 = input("Which Field Would You Like To Change?\n[FIRST NAME]"
                    " [SECOND NAME] [ADDRESS 1] [ADDRESS 2] [POST CODE]"
                    " [TEL NUMBER]: ")

user_input = user_input.upper()
user_input2 = user_input2.upper()

if user_input == "1":
    user1()
elif user_input == "2":
    user2()
elif user_input == "3":
    user3()
