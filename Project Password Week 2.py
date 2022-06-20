
password = input("Plz Type Your Password: \n")
#Must Contain At Least 8 Words
if len(password) >= 8 :
# Must Not Be Empty
    if password.isspace() != True:
#Must Contain Both Word And Numbers And Not Space Between Them
        if password.isalnum()  :
#Must Not Start With Number
            if password[0].isnumeric() != True:
            
                print("..:##:..".join(password),)
            else:
                print("Your Password Must Not Start With A Number ")

        else:
             print("Your Password Must Contain Numbers And Words And Must Not Have Space At the Begginig Or Between Characters ")
    else:
        print("Your Password Should Not Be Empty")
else:
    print("Your Password Must Have At Least 8 Charachter ")
            
