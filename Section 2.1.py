

#Nec fields to search, ID, First name, Second Name, address 1, adress 2, post code
#telephone number

import linecache




def user1():
    if user_input2 == "ID":
        ID = linecache.getline('Users.txt', 1)
        print(ID)
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

user_input = user_input.upper()
user_input2 = user_input2.upper()


if user_input == "1":
    user1()
elif user_input == "2":
    user2()
elif user_input == "3":
    user3()