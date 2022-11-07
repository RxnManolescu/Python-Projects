
import math

#First output to be displayed to user
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment   - to calculate the amount of interest you'll earn on investment")
print("bond         - to calculate the amount you'll have to pay on a home loan\n")

#Ask user to input calculation type and create a temporary variable
#Redeclare variable so that result is not dependent on input's case sensitivity
temp_variable = input("Is your calculation for an investment or bond?\n")
calculation_type = temp_variable.lower()
investment = "investment"
bond = "bond"

#if/elif/else condition is used to determine type of calculation(investment, bond or error)
if calculation_type == investment:
   inv_amount = float(input("Please enter the amount you would like to deposit:\n"))
   int_rate = float(input("Please enter the annual interest rate:\n"))
   inv_duration = float(input("Please enter the number of years:\n"))
   #Ask user for input and create a temporary variable
   #Redeclare variable so that result is not dependent on input's case sensitivity
   temp_interest = input("Please choose interest type: simple or compound?\n")
   interest = temp_interest.lower()
   simple = "simple"
   compound = "compound"
   #Annual interest rate expressed as a percentage
   int_rate_percentage = int_rate / 100
   #if/elif/else condition used to determine interest type: simple or compound or error
   if interest == simple:
      #Total amount calculated with simple interest as A = P * (1 + (r * t)) where
      #A = total_amount
      #P = inv_amount
      #r = int_rate_percentage
      #t = inv_duration
      total_amount = float(inv_amount * (1 + (int_rate_percentage * inv_duration)))
      print(f"The total amount on your investment would be {round(total_amount, 2)}!")
   elif interest == compound:
      #Total amount calculated with compound interest as A = p * math.pow((1 + r), t) where
      # math.pow function raises the first argument to the power of the second argument and
      #A = total_amount
      #P = inv_amount
      #r = int_rate_percentage
      #t = inv_duration
      total_amount = float(inv_amount * math.pow((1 + int_rate_percentage),inv_duration))
      print(f"The total amount on your investment would be {round(total_amount, 2)}!")
   else:
      #Display error message when input is not valid
      print(f"Sorry! The value you entered is not recognized!")
elif calculation_type == bond:
   #User is then asked to input house value, interest rate, duration, no of monthly repayments
   house_value = float(input("Please enter the present value of the house:\n"))
   int_rate = float(input("Please enter the annual interest rate:\n"))
   bond_duration = float(input("Please enter the number of monthly repayments:\n"))
   #Monthly interest rate expressed as a percentage
   int_rate_monthly = int_rate / (100 *12)
   #Monthly repayments calculated as A = ((i * P) / (1 - math.pow(1 + i), t) where
   #math.pow function raises the first argument to the power of the second argument and
   #A = repayments
   #P = house_value
   #i = int_rate_monthly
   #t = bond_duration
   repayments = (int_rate_monthly * house_value)
   repayments /=  (1 - math.pow(1 + int_rate_monthly, -bond_duration))
   print(f"Your monthly repayments would be {round(repayments, 2)}")
else:
   #Display error message when input is not valid
   print(f"Sorry! The value you entered is not recognized!")