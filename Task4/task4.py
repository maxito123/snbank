import os.path
import random


def operation():
    print("CHOOSE OPERATION THAT YOU WANT TO PERFORM")
    action_to_perform_loop = False
    while action_to_perform_loop is False:

        print("\n1. CREATE NEW BANK ACCOUNT\n2. CHECK ACCOUNT DETAILS\n3. LOGOUT")
        action_to_perform = input("Please enter 1 , 2 or 3 as indicated above to perform the actions: ")

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
            operation()


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
                user1 = user[1].strip("\n")
                if username == user1:
                    correct += 1
                    break
            for psw in staff_data_file:
                psw = psw.split(":")
                psw1 = psw[1].strip("\n")
                if password == psw1:
                    user1 = user[1].strip("\n")
                if username == user1:
                    correct += 1
                    break
            for psw in staff_data_file:
                psw = psw.split(":")
                psw1 = psw[1].strip("\n")
                if password == psw1:
                    correct += 1
                    break
        if correct == 2:
            print("Login successful")
            session_file = open("session.txt", "w")
            session_file.write(f"{username} is currently login")
            session_file.close()
            print("session file has been created for you")
            login_loop = True
            operation()
        else:
            print("Invalid login password or username")
            staff_login()


def create_account():
    print("WELCOME TO ACCOUNT CREATION PAGE")
    customer_data = []
    account_name = input("Enter your Account Name: ")
    account_bal = input("Enter your account Balance ")
    account_type = input("Enter your account Type: ")
    account_email = input("Enter your email: ")
    account_no = ''.join(map(str, [random.randint(0, 9) for i in range(0, 10)]))
    print("Your Account has been created, and your Account number is\n" + account_no)
    customer_file = open("customer.txt", "w+")
    customer_file.write("Account Number: %s\n" % account_no)
    customer_file.write("Account Name: %s\n" % account_name)
    customer_file.write("Account Balance: %s\n" % account_bal)
    customer_file.write("Account Type: %s\n" % account_type)
    customer_file.write("Account Email: %s\n" % account_email)
    customer_file.close()
    print("\nTHank you for choosing SnBank\n")
    operation()


def check_account_details():
    acc_detail_loop = 3

    try:
        user_account_no = int(input("Enter your Account Number: "))
        while acc_detail_loop > 0:
            if account_no == user_account_no:
                with open("customer.txt", "r") as customer_data_file:
                    for customer in customer_data_file:
                        customer = customer.split("\n")
                        print(customer)
                    acc_detail_loop = 0
            else:
                print("Wrong Account Number, please enter a valid Account Number")
                acc_detail_loop -= 1
            if acc_detail_loop == 1:
                create_account()
            else:
                check_account_details()
    except ValueError:
        print(" Invalid input, your Account Number must be Numbers")
        check_account_details()
    operation()


def close_app():
    print("Thank you for banking with us")
    quit()


def logout():
    os.remove("session.txt")
    print("You now logout")
    landing_page()


def landing_page():
    print("\nWELCOME OUR EXECUTIVE STAFF\n")
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
account_no = ""
print("WELCOME TO THE ADMINISTRATION PAGE OF STARTNG 2020 BANK")
landing_page()




# End