#QA 2nd Week Assessment
#===========================================================================================

def section1_1():
    print("")
    print("Task: Create a function which will list all the Records that are specified in the\n"
          "Text file. You may want to reformat the data to be in a single print statement,\n"
          "for better readability ")
    print("")

    with open('users.txt', 'r') as u: #Opens user.txt file in read mode

        class Resource( object ): #new class is created
            for line in 'users.txt': #iterates through the lines present in user.txt file
                class_counter= 1
                def __init__(self, ID, First_Name, Second_Name, Address_1, Address_2, Post_Code,
                            Telephone_Number):
                    self.ID = ID #ID number
                    #self.ID = Resource.class_counter
                    self.First_Name = First_Name #first name
                    self.Second_Name = Second_Name #second name
                    self.Address_1 = Address_1 #first line of address
                    self.Address_2 = Address_2 #second line of address
                    self.Post_Code = Post_Code #post code
                    self.Telephone_Number = Telephone_Number #Telephone number
                    Resource.class_counter += 1


        user = Resource(u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline())
        user2 = Resource(u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline())
        user3 = Resource(u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline())

        person1 = vars(user) #stores the data read from the file into user
        person2 = vars(user2)
        person3 = vars(user3) #iterates 3 times to ensure all user details have be obtained

    u.close()

    print('================================================')
    print ("\n".join("%s: %s" % item for item in person1.items())) #prints out the data
    print('================================================')
    print ("\n".join("%s: %s" % item for item in person2.items()))
    print('================================================')
    print ("\n".join("%s: %s" % item for item in person3.items()))
    print('================================================')

#===========================================================================================

def section1_2():
    print("")
    print("Task: Create a function that can add a person to this text file\n"
          "following the existing format.  The data for this person should be taken as user input.\n"
          "Remember the ID should be unique, so the program should auto-generate the next ID, not\n"
          "accepted as an input. ")
    print("")

    with open('users.txt', 'a+') as u: #opens file in append mode
        user_fname = input("Please Enter Your First Name: ") #user input to input their credentials
        user_sname = input("Please Enter Your Second Name: ")
        user_add1 = input("Please Enter Your First Line Of Address: ")
        user_add2 = input("Please Enter Your City: ")
        user_postcode = input("Please Enter Your Post Code: ")
        user_number = input("Please Enter Your Telephone Number: ")

        # u.readline()
        ID_Counter = 4 #automatic id generator starting from 4 instead of 0
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
        ID_Counter = + 1 #adds an increment to ID number

    u.close()

#===========================================================================================

def section1_3():
    print("")
    print("Task: Create a function to remove a particular person from this text file,\n"
          "the user should be able to pick which person they remove by specifying an ID. ")
    print("")
    user_choice = input("Which ID Would You Like To Remove?\n[1]\n[2]\n[3]")

    i = open('users.txt', 'r') #opens users.txt file in read mode
    data = i.readlines() #stores all in the lines in variable called data
    i.close() # file is closed

    f = open('sol1.txt', 'w') #creats a new txt file in which data can be copied to
    f.write(str(data)) #writes the data into the new file
    f.close()

    if user_choice == "1":
        del data[0:6 + 1] #deletes the range of the data that the person has
        f = open("UserNew.txt", "w") #opens up a new file in write mode
        f.writelines(data) #writes the new data
    elif user_choice == "2":
        del data[7:13 + 1]
        f = open("UserNew.txt", "w")
        f.writelines(data)
    elif user_choice == "3":
        del data[14:20 + 1]
        f = open("UserNew.txt", "w")
        f.writelines(data)

#===========================================================================================

def section2_1():
    print("")
    print("Task: Create a function that can list information about a person\n"
          "that exists in thetext file. The user should be able to choose which\n"
          "field to search by.")
    print("")
    import linecache #imports line cache to get any line from any file

    def user1():
        if user_input2 == "ID":
            ID = linecache.getline('Users.txt', 1) #grabs the corresponding line from txt file
            print(ID) #prints the ID
        elif user_input2 == "FIRST NAME":
            fname = linecache.getline('Users.txt', 2)
            print(fname)
        elif user_input2 == "SECOND NAME":
            sname = linecache.getline('Users.txt', 3)
            print(sname)
        elif user_input2 == "ADDRESS 1":
            add1 = linecache.getline('Users.txt', 4)
            print(add1)
        elif user_input2 == "ADDRESS 2":
            add2 = linecache.getline('Users.txt', 5)
            print(add2)
        elif user_input2 == "POST CODE":
            pcode = linecache.getline('Users.txt', 6)
            print(pcode)
        elif user_input2 == "TEL NUMBER":
            tel = linecache.getline('Users.txt', 7)
            print(tel)

    def user2():
        if user_input2 == "ID":
            ID = linecache.getline('Users.txt', 8)
            print(ID)
        elif user_input2 == "FIRST NAME":
            fname = linecache.getline('Users.txt', 9)
            print(fname)
        elif user_input2 == "SECOND NAME":
            sname = linecache.getline('Users.txt', 10)
            print(sname)
        elif user_input2 == "ADDRESS 1":
            add1 = linecache.getline('Users.txt', 11)
            print(add1)
        elif user_input2 == "ADDRESS 2":
            add2 = linecache.getline('Users.txt', 12)
            print(add2)
        elif user_input2 == "POST CODE":
            pcode = linecache.getline('Users.txt', 13)
            print(pcode)
        elif user_input2 == "TEL NUMBER":
            tel = linecache.getline('Users.txt', 14)
            print(tel)

    def user3():
        if user_input2 == "ID":
            ID = linecache.getline('Users.txt', 15)
            print(ID)
        elif user_input2 == "FIRST NAME":
            fname = linecache.getline('Users.txt', 16)
            print(fname)
        elif user_input2 == "SECOND NAME":
            sname = linecache.getline('Users.txt', 17)
            print(sname)
        elif user_input2 == "ADDRESS 1":
            add1 = linecache.getline('Users.txt', 18)
            print(add1)
        elif user_input2 == "ADDRESS 2":
            add2 = linecache.getline('Users.txt', 19)
            print(add2)
        elif user_input2 == "POST CODE":
            pcode = linecache.getline('Users.txt', 20)
            print(pcode)
        elif user_input2 == "TEL NUMBER":
            tel = linecache.getline('Users.txt', 21)
            print(tel)

    user_input = input("Which ID Would You Like To View?\n[1] [2] [3]: ")
    user_input2 = input("Which Field Would You Like To View?\n[ID] [FIRST NAME]"
                        " [SECOND NAME] [ADDRESS 1] [ADDRESS 2] [POST CODE]"
                        "[TEL NUMBER]: ")

    user_input = user_input.upper() #converts user input into capitals
    user_input2 = user_input2.upper()

    if user_input == "1":
        user1()
    elif user_input == "2":
        user2()
    elif user_input == "3":
        user3()

#===========================================================================================

def section2_2():
    print("")
    print("Task: Create a function that can make a copy of the text file to be used\n"
          "as a back-up. (hint: research shutil.copy())")
    print("")
    import shutil

    shutil.copy('users.txt', 'UsersBackup.txt')

#===========================================================================================

def section2_3():
    print("")
    print("Task: Create a function to update a person that already exists in the text\n"
          "file, theuser should be able to pick which record they update and which\n"
          "field in the record they change.(hint: research .strip() to remove new line characters)")
    print("")


    with open('users.txt', 'r') as file:
        data = file.readlines()

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
            data[4] = (add2_ + "\n")
            with open('users.txt', 'w') as file:
                file.writelines(data)
        elif user_input2 == "POST CODE":
            print("Current: " + data[5])
            pcode = input("Please Enter New Post Code: ")
            print("Updated: " + pcode)
            data[5] = (pcode + "\n")
            with open('users.txt', 'w') as file:
                file.writelines(data)
        elif user_input2 == "TEL NUMBER":
            print("Current: " + data[6])
            tel = input("Please Enter New Tel Number: ")
            print("Updated: " + tel)
            data[6] = (tel + "\n")
            with open('users.txt', 'w') as file:
                file.writelines(data)


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
            data[11] = (add2_ + "\n")
            with open('users.txt', 'w') as file:
                file.writelines(data)
        elif user_input2 == "POST CODE":
            print("Current: " + data[12])
            pcode = input("Please Enter New Post Code: ")
            print("Updated: " + pcode)
            data[12] = (pcode + "\n")
            with open('users.txt', 'w') as file:
                file.writelines(data)
        elif user_input2 == "TEL NUMBER":
            print("Current: " + data[13])
            tel = input("Please Enter New Tel Number: ")
            print("Updated: " + tel)
            data[13] = (tel + "\n")
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
            data[18] = (add2_ + "\n")
            with open('users.txt', 'w') as file:
                file.writelines(data)
        elif user_input2 == "POST CODE":
            print("Current: " + data[19])
            pcode = input("Please Enter New Post Code: ")
            print("Updated: " + pcode)
            data[19] = (pcode + "\n")
            with open('users.txt', 'w') as file:
                file.writelines(data)
        elif user_input2 == "TEL NUMBER":
            print("Current: " + data[20])
            tel = input("Please Enter New Tel Number: ")
            print("Updated: " + tel)
            data[20] = (tel + "\n")
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

#=======================================================================================================================

def section3():
    print("View Duplicate Fields?:\n"
          "Yes = [Y]\n"
          "No = [N]")


    with open('users.txt', 'r') as file:

        data = file.readlines()

    user_input2 = input(":")
    user_input2 = user_input2.upper()
    def user1():
        if user_input2 == "Y":
            print("Male 1: " + data[1])
            print("Male 2: " + data[15])

    user1()



#=======================================================================================================================

marker = input("Which Section Would You Like To View?\nSection 1.1 = [1.1]\n"
               "Section 1.2 = [1.2]\nSection 1.3 = [1.3]\nSection 2.1 = [2.1]\n"
               "Section 1.1 = [2.2]\nSection 2.3 = [2.3]\nSection 3 = [3]")

marker = marker.upper()

if marker == "1.1":
    section1_1()
elif marker == "1.2":
    section1_2()
elif marker == "1.3":
    section1_3()
elif marker == "2.1":
    section2_1()
elif marker == "2.2":
    section2_2()
elif marker == "2.3":
    section2_3()
elif marker == "3":
    section3()

#=======================================================================================================================

