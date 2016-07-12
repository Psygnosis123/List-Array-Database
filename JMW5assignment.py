print("Welcome to the Team Manager")
print("To navigate the menu, type the number shown, otherwise, type '9' to cancel. ")

userchoice = 0
userinfo=[]
#usernumber={}
#userjersey={}

while userchoice != 9:

    print("Main Menu")
    print("------------")
    print("1. Display Name(s)")
    print("2. Add Name(s) & Phone Number(s) & Jersey Number")
    print("3. Remove Name")
    print("4. Edit Name")
    print("5. Save Information")
    print("6. Load Data")
    print("9. Cancel Program")

    # print("5. Display Phone Number(s)")
    # print("6. Display Jersey Number(s)")

    userchoice = int(input("Your input?"))

    if userchoice == 1:
        current = 0
        if len(userinfo) > 0:
            while current < len(userinfo):
                print(current, ".", userinfo[current])
                current = current + 1
        else:
            print("Your list is empty.")
    elif userchoice == 2:
        username = input("Please, type in your name. ")
        userinfo.append(username)
        userphone = int(input("Please, enter phone number. "))
        usernumber[username] = userphone
        userjerseynum = int(input("Please, enter the Jersey number. "))
        userjersey[username] = userjerseynum
    elif userchoice == 3:
        del_username = input("Please, type in the name you would like to remove. ")
        print("Your name was removed. ")
        if del_username in userinfo:
            userinfo.remove(del_username)
        else:
            print(del_username, "Error, your name was not found. ")
    elif userchoice == 4:
        old_user = input("Type in the name you would like to change. ")
        if old_user in userinfo:
            user_number = userinfo.index(old_user)
            new_user = input("What is your new name? ")
            userinfo[user_number] = new_user
        else:
            print(old_user, "Your name was not found. ")
    elif userchoice == 5:
        for x in usernumber.keys():
            print("Name: ", x, "\tNumber:", usernumber[x])
    elif userchoice == 6:
        for x in userjersey.keys():
            print("Name: ", x, "\tJersey:", userjersey[x])

print("Thank you, Please close this window. ")