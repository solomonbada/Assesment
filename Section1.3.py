#if searched for male print mark and geoff

print("View Duplicate Fields?:\n"
      "Yes = [Y]\n"
      "No = [N]")
with open('users.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

user_input2 = input(":")


def user1():
    if user_input2 == "Y":
        print("Male 1: " + data[1])
        print("Male 2: " + data[15])


user1()