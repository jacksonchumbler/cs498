import pandas as pd
import sys

user_df = pd.read_csv('users.csv')
form_df = pd.read_csv('forms.csv')
current_user = "invalid_user"

def main():
    
    login()
    menu()

    print(user_df)
    print(form_df)
    user_df.to_csv('users.csv', index = False) 
    form_df.to_csv('forms.csv', index = False) 

def menu():
    global current_user
    while True:
        print("\nWelcome, {}, to the Coroner Database".format(user_df.loc[user_df['email'] == current_user, 'name'].item()))
        print("Available Operations:")
        print("Create New Form [0]")
        print("View Form       [1]")
        print("Secure Logout   [2]")

        choice = int(input('Enter a choice: '))
        print()
        if   choice == 0:
            form()
        elif choice == 1:
            view()
        elif choice == 2:
            # Securely clears login
            current_user = ""
            break 
        else: 
            print("Invalid Input!")

def form():
    print("Please provide the following information...")
    name_d = input("Name of Deceased: ")
    place_d = input("Address of Death: ")
    time_d = input("Death Time: ")
    form_df.loc[len(form_df)] = [current_user, name_d, place_d, time_d]
    print()

def view():
    # print("Under Construction!")
    print(form_df.loc[form_df['author'] == current_user])
    return

def logout():
    pass

def login():
    attempts = 0
    user_type = input('Are you a (new/existing) user?\n')
    if user_type == 'new':
        generate_user()
        print("Successfully Added Account")
    while attempts < 3:
        print("\nPlease Login...")
        email = input('Enter login email: ')
        passwd = input('Enter Password: ')

        if email in user_df['email'].values:
            login_user = user_df.loc[user_df['email'] == email]
            if passwd in login_user['passwd'].values:
                global current_user
                current_user = email
                return
        print("\nIncorrect Login")
        attempts += 1
    print("\nExceeded Login Retries")
    sys.exit()

def generate_user():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    passwd  = input('Enter your password: ')
    user_df.loc[len(user_df)] = [name, email, passwd] 
    return 

if __name__ == '__main__':
    main()
