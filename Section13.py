user_choice = input("[1] [2] [3]: ")

i = open('users.txt', 'r')
data = i.readlines()
i.close()

f = open('sol1.txt', 'w')
f.write(str(data))
f.close()



if user_choice == "1":
    del data[0:6 +1]
    f = open("UserNew.txt", "w")
    f.writelines(data)
elif user_choice == "2":
    del data[7:13 +1]
    f = open("UserNew.txt", "w")
    f.writelines(data)
elif user_choice == "3":
    del data[14:20 +1]
    f = open("UserNew.txt", "w")
    f.writelines(data)

#for first person index is [0:6 +1], second person [7:13 +1], third [8:20 +1]