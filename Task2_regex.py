import re

def valid_email(email):
    return re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Za-z]+', email)

def write_to_file(email):
    with open("regex_file.txt", "a") as f:
        f.write(email + '\n')

def read_emails_from_file():
    with open("regex_file.txt", "r") as f:
        emails = f.readlines()
        for e in emails:
            print(e.strip())

while True:
    user_choice = input("Do you want to enter email? (yes/no): ").strip().lower()

    if user_choice == 'yes':
        input_email = input("Enter any email: ")
        if valid_email(input_email):
            write_to_file(input_email)
            print("Email is valid and written into file.")
        else:
            print("Invalid format.")

    elif user_choice == "no":
        print("Emails from the file:")
        read_emails_from_file()
        break

    else:
        print("Invalid choice, please enter yes or no.")




