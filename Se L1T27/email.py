#An SMS Simulation


class Email:

    # constructor method with instance variables
    def __init__(self, email_contents, from_address, has_been_read = False, is_spam = False):
        self.email_contents = email_contents
        self.from_address = from_address
        self.has_been_read = has_been_read
        self.is_spam = is_spam

    # Method to mark emails as read
    def mark_as_read(self):
        self.has_been_read = True

    # Method to mark emails as spam
    def mark_as_spam(self):
        self.is_spam = True

    # Method to return the object representation in a string format
    def __repr__(self):
        return  f"\nEmail from:   {self.from_address} \n"\
                f"Email read:   {self.has_been_read}\n"\
                f"Spam email:   {self.is_spam}\n"\
                f"Message:      \"{self.email_contents}\"\n"


# Function  to take user input, create a new Email object and store it in a list
def add_email():
        email_contents = input("Please enter the contents of the email:\n")
        from_address = input("Please enter the sender's email address:\n")
        new_email = Email(email_contents, from_address)
        inbox.append(new_email)


#Function to display all emails stored in list
def all_emails():
    print("\nPLEASE SEE BELOW ALL YOUR EMAILS:\n")
    for idx, i in enumerate(range(len(inbox)), start = 1):
        print(f"\nEmail number: {idx} {inbox[i]}")


# Function to get the number of emails in the list
def get_count():
    print(f"\nThe number of emails in the inbox is now {len(inbox)}.\n")


# Function to return all unread emails and their index position
def get_unread_emails():
    for idx, i in enumerate(range(len(inbox)), start = 1):
        if inbox[i].has_been_read == False:
            print(f"\nEmail number: {idx} {inbox[i]}")


# Function to allow to mark unread emails as read.
# When user enters "0" they are returned to main menu
def get_email():
    all_emails()
    while True:
        # Try/Except block to handle Value Errors raising due to inaccurate user input
        try:
            email_request = int(input("Please enter the email number you'd like to mark as read. "\
                           "Please enter \"0\" to return to main menu: "))
            # Variable to match user input with emails index
            read_index = email_request -1

            # Conditions to check user input and mark emails as read or display relevant message
            if read_index in range(len(inbox)):
                if inbox[read_index].has_been_read == False:
                    result = inbox[read_index]
                    result.has_been_read = True
                    print("\n--> SUCCESS! Email marked as \"read\"!\n")
                    get_unread_emails()
                else:
                    print("\n--> This email has already been marked as read!\n")
                    get_unread_emails()
            elif read_index == -1:
                break
            else:
                print("\n--> Email index invalid. Please try again!\n")
                get_unread_emails()
        except ValueError:
            print("\n--> Number input required!\n")


# Function to return all emails marked as spam and their index positions
def get_spam_emails():
    for idx, i in enumerate(range(len(inbox)), start = 1):
        if inbox[i].is_spam == True:
            print(f"\nEmail number: {idx} {inbox[i]}")
            spam_emails.append(i)


# Function to allow to mark as spam all relevant emails
# When user enters "0" they are returned to main menu
def mark_as_spam():
    all_emails()
    while True:
        # Try/Except block to handle Value Errors arising due inaccurate user input
        try:
            spam_request = int(input("Please choose the email number you'd like to mark as spam. "\
                          "Please enter \"0\" to return to main menu: "))
            # Variable to match user input with emails index
            spam_index = spam_request -1

            # Conditions to check user input and mark emails as spam or dispaly relevant message
            if spam_index in range(len(inbox)):
                if inbox[spam_index].is_spam == False:
                    inbox[spam_index].is_spam = True
                    print("\n--> SUCCESS! This email has been marked as \"spam\"!\n")
                else:
                    print("\n--> This email has already been marked as spam!\n")
            elif spam_index == -1:
                break
            else:
                print("\n--> Email index invalid! Please try again!\n")
        except ValueError:
            print("\n--> Number input required!\n")


# Function to delete an email chosen by user
def delete():
    while True:
        all_emails()
        if len(inbox) != 0:
            # Try/Except block to handle Value Errors arising due inaccurate user input
            try:
                delete_request = int(input("Please enter the email number you would like "\
                                "to delete: Please enter \"0\" to return to main menu: "))
                # Variable to match user input with emails index
                delete_index = delete_request - 1

                # Conditions to check user input and allow to delete or dispaly relevant message
                if delete_index in range(len(inbox)):
                    inbox.pop(delete_index)
                    print("\n--> SUCCESS! The email has now been deleted!\n")
                elif delete_index == -1:
                    break
                else:
                    print("\n--> Email index invalid! Please try again!\n")
            except ValueError:
                print("\n--> Number input required!\n")
        else:
            print("No emails found!")
            break


# Empty lists
inbox = []
spam_emails = []

# Initial objects creation and appending the objects to the empty list
trial_email1 = Email("Trial content 1", "trial1@outlook.com")
inbox.append(trial_email1)
trial_email2 = Email("Trial content 2", "trial2@gmail.com")
inbox.append(trial_email2)
trial_email3 = Email("Trial content 3", "trial3@yahoo.com")
inbox.append(trial_email3)


user_choice = ""

# Loop to allow user to choose menu options
while user_choice != "quit":
    user_choice = input("Please choose an option - read/mark spam/send/delete/quit: ").lower()
    # Allow user to read existing emails in list
    if user_choice == "read":
        get_email()
    # Allow user to mark emails as spam
    elif user_choice == "mark spam":
        mark_as_spam()
        # Provide user with the option to view spammed emails
        while True:
            spam_choice = input("Would you like to view your spam emails? yes or no? ").lower()
            if spam_choice == "yes":
                get_spam_emails()
                if len(spam_emails) == 0:
                    print("\n--> No spam emails found!")
                break
            elif spam_choice == "no":
                break
            else:
                print("Wrong choice! Please try again!")
    # Allow user to create a new email object and display the number of emails in the inbox
    elif user_choice == "send":
        add_email()
        get_count()
    # Allow user to delete existing emails
    elif user_choice == "delete":
        delete()
    elif user_choice == "quit":
        print("Goodbye!")
    else:
        print("Oops - incorrect input!")
