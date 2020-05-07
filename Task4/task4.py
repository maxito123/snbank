import os
import random


def staff_login():
    print("Welcome to Staff Login Page")
    correct = 0
    login_loop = False

    while login_loop is False:

        username = input("\nPlease enter your username: ")
        password = input("\nEnter your Password: ")
        with open("staff.txt", "r") as staff_data_file:
            for user in staff_data_file:
                user = user.split(":")
                #print(user)
                user1 = user[1].strip("\n")
                if username == user1:
                   # print(user1)
                    correct += 1
                    break

            for psw in staff_data_file:
                psw = psw.split(":")
                #print(psw)
                psw1 = psw[1].strip("\n")
                if password == psw1:
                    # print(user1)
                    correct += 1
                    break
        if correct == 2:
            print("Login successful")
        session_file = open("session.txt", "w")
        session_file.write(f"{username} is currently login")
        print("session file has been created for you")
        login_loop = True


def create_account():
    print("WELCOME TO ACCOUNT CREATION PAGE")
    customer_data = []
    account_name = list(input("Enter your Account Name: ").upper())
    account_bal = input("Enter your account Balance ")
    account_type = input("Enter your account Type: ")
    email = input("Enter your email: ")
    account_no = random.randint()
    print("Your Account has been created, and your Account number is\n"+account_no)
    customer_data.append(account_name)
    customer_data.append(account_bal)
    customer_data.append(account_type)
    customer_data.append(email)
    customer_data.append(account_no)



def close_app():
    print("Thank you for banking with us")
    quit()


def logout():
    os.remove("session.txt")
    print("You now logout")
    landing_page()


def landing_page():
    print("Staff Login\nClose App\n")
    action = input("Please select from the above action to perform by entering ' L' for login and"
                   " 'C' to close App\n > ").upper()
    if action == "L":
        staff_login()
    elif action == "C":
        close_app()
    else:
        print("Invalid selection, Please try again")
        landing_page()



# Main Program
print("WELCOME TO THE ADMINISTRATION PAGE OF STARTNG 2020 BANK")
landing_page()

action_to_perform_loop =False
while action_to_perform_loop is False:
    print("\n1. CREATE NEW BANK ACCOUNT\n2. CHECK ACCOUNT DETAILS\n3. LOGOUT")
    action_to_perform = input("Please enter 1 , 2 or 3 as indicated above to perform the actions")
    if action_to_perform == "1":
        create_account()
        action_to_perform_loop = True
    elif action_to_perform == "2":
        check_account_details()
        action_to_perform_loop = True
    elif action_to_perform == "3":
        logout()
        action_to_perform_loop = True
    else:
        print("Invalid selection, try again")
