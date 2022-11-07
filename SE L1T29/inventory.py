

from tabulate import tabulate


class Shoe:
    
    # Constructor method with instance variables
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Method to get the cost of each object
    def get_cost(self):
        return self.cost

    # Method to get the quantity of each object
    def get_quantity(self):
        return self.quantity

    # Method to get the value of each object by multiplying its cost and quantity
    def get_value(self):
        return int(self.cost) * int(self.quantity)

    # Method to return the string representation of the object to improve readability
    def __repr__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n"


# Funtion to read data from text file as objects and store it in list of objects
def read_shoes_data():

    try:
        with open("inventory.txt" , "r") as file:
            data = file.readlines()

            for line in data:
                if line == "" or line =="\n":
                    continue
                else:
                    item = line.rstrip("\n").split(",")
                    shoe_entry = Shoe(item[0], item[1], item[2], item[3], item[4])
                    shoes.append(shoe_entry)
    except FileNotFoundError:
        print("Sorry, file not found!")
        exit()


# Function to allow user to create a new shoe object
def capture_shoes():

    print("Please fill in the following options:\n")
    country = input("Country of origin: ")
    if country != "":
        product = input("Product name: ")
        if product != "":
            # Try/Except blocks to condition user input type
            while True:
                try:
                    codes = int(input("Product SKU: "))
                    code = "SKU" + str(codes)
                    break
                except ValueError:
                    print("--> Number required!")
            while True:
                try:
                    cost = int(input("Product cost: "))
                    break
                except ValueError:
                    print("--> Number required!")
            while True:
                try:
                    quantity = int(input("Product quantity: "))

                    # New object creation with user input
                    new_entry = f"{Shoe(country, code, product, cost, quantity)}"
                    shoes.append(new_entry)
                    print("--> SUCCESS! Product added to the inventory!\n")
                    break
                except ValueError:
                    print("--> Number required!")
        else:
            print("--> Product entry error! Please try again!")
    else:
        print("--> Country entry error! Please try again!")

    # Writing the new object to the text file
    with open("inventory.txt", "w") as file:
        for line in shoes:
            file.write(f"{line}")


# Function to display all shoe objects in a table format
def view_all():

    for i in shoes:
        temp_shoe = [i.country, i.code, i.product, i.cost, i.quantity]
        inventory.append(temp_shoe)
    shoes_table = tabulate(inventory, headers = "firstrow", tablefmt = "grid")
    print(shoes_table + "\n")


# Function to allow user to re-stock the shoe object with the lowest quantity
def re_stock():

    # Assign the lowest quantity to the first shoe in the list
    lowest_shoe = shoes[1]

    for shoe in shoes[1:]:
        try:
            # Condition to compare all shoes in the list with the precedent one
            if int(shoe.get_quantity()) <= int(lowest_shoe.get_quantity()):
                lowest_shoe = shoe
        except ValueError:
            continue

    print(f"\nLowest quantity shoes:\n{lowest_shoe}\n")

    # Ask user to update quantity 
    new_quantity = input("Please enter the new quantity: ")

    # Condition to check user input's validity and assign new input as the new quantity
    # or print error message when input is not valid
    if new_quantity != "":
        lowest_shoe.quantity = new_quantity
        print("--> SUCCESS! The inventory has now been updated!\n")

        # Overwrite file with the new updated quantity
        with open("inventory.txt", "w") as file:
            for line in shoes:
                    file.write(f"{line}")
    else:
        print("Sorry! The number entered was not valid!")


# Function to allow user to search for a shoe by inputting the shoe code,
# display shoe or display message if shoe not found
def search_shoe():

    code_input = input("Please enter the product code(ie SKU12345): ")

    shoe_found = False

    for shoe in shoes:
        if shoe.code == code_input:
            shoe_found = True
            print(f"Product:   {shoe.product}\n"\
                f"Code:      {shoe.code}\n"\
                f"Country:   {shoe.country}\n"\
                f"Cost:      {shoe.cost}\n"\
                f"Quantity:  {shoe.quantity}\n")

    if shoe_found == False:
        print("--> Shoe not found!")


# Funcion to retrieve and display the values of all shoes making use of the tabulate module
# and the get_value() method
def value_per_item_two():

    for shoe in shoes[1:]:
        new_value = [shoe.product, shoe.get_value()]
        values.append(new_value) # Append all shoes and values to a separate list
    values_table = tabulate(values, headers = ["Product", "Value"], tablefmt = "grid")
    print(values_table + "\n")


# Function to display the shoe with the highest quantity
def highest_qty():

    #Assign the highest quantity to the first shoe on the list
    highest_shoe = shoes[1]

    for shoe in shoes[1:]:
        # Condition to compare all shoes in the list with the precedent one
        if int(shoe.get_quantity()) >= int(highest_shoe.get_quantity()):
            highest_shoe = shoe
    print("Below shoes have the highest quantity and are now ON SALE:") 
    print(f"Product:   {highest_shoe.product}\n"\
        f"Code:      {highest_shoe.code}\n"\
        f"Country:   {highest_shoe.country}\n"\
        f"Cost:      {highest_shoe.cost}\n"\
        f"Quantity:  {highest_shoe.quantity}\n")


# Function to display main menu to user making use of all the functions above
def main():

    # Start with an empty list
    shoes.clear()

    # Call function to retrieve all shoes data
    read_shoes_data()

    # Loop to allow user to return to main menu and choose different option until
    # user chooses to exit
    while True:
        menu = input("""Please choose one of the following options:
                        1 - View all shoes
                        2 - Search shoes
                        3 - Add shoes
                        4 - View shoes value
                        5 - Shoes on sale
                        6 - Re-stock shoes
                        0 - Exit
                        --> """)
        # Conditions block to call functions according to user choice
        if menu == "1":
            view_all()
        elif menu == "2":
            search_shoe()
            # Loop to allow user to choose whether they want to search more than one shoe
            # before returning them to the main menu
            while True:
                choice = input("""Would you like to search another product?
                        1 - yes
                        2 - no
                        --> """)
                if choice == "1":
                    search_shoe()
                elif choice == "2":
                    main()
                else:
                    print("--> Choice invalid! Please try again!")
        elif menu == "3":
            capture_shoes()
            # Loop to allow user to add more than one new product at a time
            # before returning them to the main menu
            while True:
                choice = input("""Would you like to add another product?
                        1 - yes
                        2 - no
                        --> """)
                if choice == "1":
                    capture_shoes()
                elif choice == "2":
                    main()
                else:
                    print("--> Choice invalid! Please try again!")
        elif menu == "4":
            value_per_item_two()
        elif menu == "5":
            highest_qty()
        elif menu == "6":
            re_stock()
            # Loop to allow user to re-stock more than one item at a time
            # before returning them to the main menu
            while True:
                choice = input("""Would you like to add another product?
                        1 - yes
                        2 - no
                        --> """)
                if choice == "1":
                    re_stock()
                elif choice == "2":
                    main()
                else:
                    print("--> Choice invalid! Please try again!")
        elif menu == "0":
            print("GOODBYE!")
            exit()
        else:
            print("--> Option invalid! Please try again!")

# List of shoes objects
shoes = []

# List of all shoes list
inventory = []

# List of all shoes and their values
values = []


main()

