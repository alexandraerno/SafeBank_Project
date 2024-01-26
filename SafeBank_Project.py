
username = ""
user_db = []
user = {"username": "", "password": "", "balance": 0.0}

def deposit():
# Asking user for input and adding the amount to the value connected to the given username in the dictionary
    for user in user_db:
        if user["username"] == username:
            amount = float(input("Please enter the amount you wish to deposit: "))
            user["balance"] += amount
            print(f"You have deposited £{amount}. Your new balance is: £{user["balance"]}\n")
            break

def balance():
# Asking user for username and displaying the balance from the dictionary
    for user in user_db:
        if user["username"] == username:
            print(f"Hi, {user["username"]}, your current balance is: £{user["balance"]}\n")
            break

def withdrawal():
# Asking user for input and subtracting the amount from the value connected to the given username in the dictionary
    for user in user_db:
        if user["username"] == username:
            amount = float(input("Please enter the amount you wish to withdraw: "))
            if amount <= user["balance"]:
                user["balance"] -= amount
                print(f"Withdrawal successful. Your new balance is £{user["balance"]}\n")
            else: 
                print("Not enough funds. Back to main menu.")

def transfer_samebank():
# Asking for user input
    receiver_found = False
    receiver_name = input("Please enter the name of the recipient: ")

    receiver = None 

    # Ensuring the user is found in the dictionary
    for receiver in user_db:
        if receiver["username"] == receiver_name:
            print("User found.")
            receiver_found = True
            break
    if not receiver_found:
        print("Not found")
        return

    # Asking for input if user is found
    for user in user_db:
        if user["username"] == username:
            amount = float(input("Please enter the amount your wish to transfer: "))
            if amount <= user["balance"]:

                # Subtracting the amount from the value connected to the username in the dictionary
                user["balance"] -= amount

                # Adding the amount to the value connected to the other username in the dictionary
                receiver["balance"] += amount
                print(f"Transfer successful. Your new balance is £{user["balance"]}\n")
            else: 
                print("Not enough funds. Back to main menu.")

def bank_options():
# Menu showing all the available options and asking for user input
    while True:
        choice = input("Please select one of the following options:\n Check balance \n Withdrawal \n Deposit \n Transfer \n Logout\n")
        if choice.lower() == "check balance":
            balance()
        elif choice.lower() == "deposit":
            deposit()
        elif choice.lower() == "withdrawal":
            withdrawal()
        elif choice.lower() == "transfer":
            transfer_samebank()
        elif choice.lower() == "logout":
            print("You have logged out")
            break
        else: 
            print("Invalid input.")
        
while True:
    # Asking for user input
    print("Welcome to SafeBank! How can we help you today?")
    user_input = input("If you wish to log into your account, type 'Login' or if you wish to register a new account, type 'Register'. Enter stop to exit.\n")

    if user_input.strip() == "register": 
        username = input("Please enter your desired username: ").strip()
        password= input("Please enter your desired password: ") 
        
        # Ensuring the username does not already exist
        is_unique = True
        for account in user_db: 
           if account ["username"] == username:
                is_unique = False

        # Adding username and password to the dictionary
        if is_unique: 
            user_db.append({"username": username, "password": password, "balance": 0.0})
            print("User registered. Back to main menu.\n")
        else:
            print("Cannot register user, username taken.")

    # Asking for user input
    elif user_input.strip() == "login":
        username = input("Please enter your username: ").strip() 
        password= input("Please enter your password: ") 

        # Checking if username and password exist in the dictionary
        for account in user_db:
            if account ["username"] == username:
                if account["password"] == password:
                    print("Welcome!\n")
                    bank_options()
                else:
                    print("Sorry, wrong password")
    
    # Break if user enters "stop"
    elif user_input == "stop":
        print("Goodbye!")
        break
    
    else:
        print("Invalid input, please try again.")

