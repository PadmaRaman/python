import random

def admin_enter():
    admin = random.randint(1,3)
    print (admin)
    if admin==1:
        user = user_enter()
        
        if user=="1":
            print ("Tie")
            admin_enter()
        elif user=="2":
            print ("user win")
            admin_enter()
        elif user=="3":
            print ("user lose")
            admin_enter()
        else:
            print ("Invalid input")
            admin_enter()
            

    elif admin==2:
        user = user_enter()
        
        if user=="1":
            print ("User lose")
            admin_enter()
        elif user=="2":
            print ("Tie")
            admin_enter()
        elif user=="3":
            print ("User win")
            admin_enter()
        else:
            print ("Invalid input")
            admin_enter()

    else:
        user = user_enter()
        
        if user=="1":
            print ("User lose")
            admin_enter()
        elif user=="2":
            print ("User win")
            admin_enter()
        elif user=="3":
            print ("Tie")
            admin_enter()
        else:
            print ("Invalid Input")
            admin_enter()
    

def user_enter():
    roll = input ("Press Y to continue, enter to quit\t")
    if roll=="y" or roll=="Y":
        user = input("Enter 1. Stone\n \
    2. Paper\n \
    3. Scissors\n")
        return user
    else:
        print("Thanks for playing, See u soon")
        exit()


admin_enter()
