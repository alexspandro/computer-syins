# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor

def printMenu():
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def enterCustomerInfo():
CustFirstName = input("Type the Customer's first name:")
CustLastName = input("Type the Customer's LAst Name:")
CustPCode = input("Type the customer's Postal Code:")
CustCCard = input("type the customer's Credit Card:")

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validatePostalCode():
file = open("postal_codes.csv", "r")
  
postalCodesFile = open("postal_codes.csv", "r")
postalCodes = postal_codes_file.read().splitlines()

print(CustPCode)


valid = False
for code in postal_codes:
    if CustPCode == code:
        valid = True
        break

if valid:
    print("The customer's postal code,", CustPCode, "is valid.")
else:
    print("The postal code", CustPCode, "is invalid.")


'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validateCreditCard():

  sumOddDigits = 0
  sumEvenDigits = 0
  total = 0
cardNumber = input("Enter a credit card #:")
cardNumber = [::-1]
print(cardNumber)

for x in cardNumber[::]:
  sumOddDigits += int(x)

for x in cardNumber[1::2]:
  x = int(x) * 2
  if x >= 10:
    sumEvenDigits += (1 + (x % 10))
  else:
    sumEvenDigits += x

  total = sumOddDigits + sumEvenDigits

  if total % 10 == 0:
    print("valid")
  else:
    print("invalid")
 

  
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def generateCustomerDataFile():
    pass    # Remove this pass statement and add your own code below

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################

####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################
'''
# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        enterCustomerInfo()

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")
'''
