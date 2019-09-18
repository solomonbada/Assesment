
with open('users.txt', 'r') as u:

    class Resource( object ):
        for line in 'users.txt':
            class_counter= 1
            def __init__(self, ID, First_Name, Second_Name, Address_1, Address_2, Post_Code,
                        Telephone_Number):
                self.ID = ID
                #self.ID = Resource.class_counter
                self.First_Name = First_Name
                self.Second_Name = Second_Name
                self.Address_1 = Address_1
                self.Address_2 = Address_2
                self.Post_Code = Post_Code
                self.Telephone_Number = Telephone_Number
                Resource.class_counter += 1

    #for line in 'user.txt':
    user = Resource(u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline())
    user2 = Resource(u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline())
    user3 = Resource(u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline(), u.readline())
    #user_ = u.read(400)
    person1 = vars(user)
    person2 = vars(user2)
    person3 = vars(user3)

u.close()

print('================================================')
print ("\n".join("%s: %s" % item for item in person1.items()))
print('================================================')
print ("\n".join("%s: %s" % item for item in person2.items()))
print('================================================')
print ("\n".join("%s: %s" % item for item in person3.items()))
print('================================================')
