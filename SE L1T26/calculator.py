

#function to take user input and print it to output file while handling input errors
def calculator():
    #while loop to ask user continuously for numbers until input matches criteria
    while True:
        #open/create output file
        with open("calculator.txt", "w+") as file:
            #ask user to input two numbers and handle input errors accordingly
            try: 
                number1 = float(input("Please enter the first number: "))
                number2 = float(input("Please enter the second number: "))
                numbers_output = f"The results of operations for {number1} and {number2} are:\n"
                file.write(numbers_output + "\n")
            except Exception:
                print("Sorry! The number you entered is not valid! Please try again!")
            #while loop to ask user continuously for operations input until user decides to stop
            while True:
                operation = input("Please enter \"+\", \"-\", \"*\" or \"/\" according "\
                    "to the desired operation or \"e\" to exit: ")

                #condition statement to calculate, print and write sum of to user input 
                if operation == "+":
                    num_sum = round(number1 + number2, 2)
                    num_sum_output = f"The sum of {number1} and {number2} is {num_sum}."
                    print(num_sum_output)
                    file.write(num_sum_output + "\n")

                #condition statement to calculate, print and write subtraction of user input
                elif operation == "-":
                    num_sub = round(number1 - number2, 2)
                    num_sub_output = f"The subtraction of {number1} and {number2} is {num_sub}."
                    file.write(num_sub_output + "\n")
                    print(num_sub_output)

                #condition statement to calculate, print and write product of user input
                elif operation == "*":
                    num_prod = round(number1 * number2, 2)
                    num_prod_output = f"The product of {number1} and {number2} is {num_prod}."
                    file.write(num_prod_output + "\n")
                    print(num_prod_output)

                #condition statement to calculate, print and write division of user input
                #avoiding division if any input is 0
                elif operation == "/" and number1 != 0 and number2 != 0:
                    num_div = round(number1 / number2, 2)
                    num_div_output = f"The division of {number1} and {number2} is {num_div}."
                    file.write(num_div_output + "\n")
                    print(num_div_output)
                
                #condition statement to exit loop
                elif operation.lower() == "e":
                    print("Goodbye!")
                    exit()

                #error message if operations choice is not valid
                else:
                    print("Sorry, operation not recognized! Please try again!")


#function to allow user to either enter the numbers and operations required, or
#to enter the file name which they would like to read the results from
def calculator_choice():
    #while loop to continuously ask user for a choice until user decides to stop
    while True:
        choice = input("Please choose from the following options:\n"\
            "1 - to input your numbers and operations\n"\
            "2 - to enter the file name you'd like to read the results from\n"\
            "e - to exit\n"
            ":")

        #contidional statement to call calculator() function should user decide to input details
        if choice == "1":
            calculator()

        #conditional statement to ask user for file name
        elif choice == "2":
            file_input = input("Please enter the file name you'd like to read the results from: ")
            #while loop to ask user continously for a file when file not found
            while True:
                try:
                    with open(file_input, "r+") as file:
                        print("\n".join(file.read().splitlines()))
                        break
                except FileNotFoundError:
                    print("The file you are trying to open does not exist! Please try again!")
                    file_input = input("Please enter the file name you'd like to read the results from: ")
        
        #conditional statement to exit loop
        elif choice.lower() == "e":
            print("Goodbye!")
            exit()
        
        #print error message when choice not recognized
        else:
            print("Sorry, you have made a wrong choice! Please try again!")


calculator_choice()