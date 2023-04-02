# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import os
#creates global variable
CustFirstName = ""
CustLastName = ""
CustCity = ""
CustPCode = ""
CustCCard = ""

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

def enterCustomerInfo():
#lets code know to make variables global
  global CustFirstName, CustLastName, CustCity, CustPCode, CustCCard
  CustFirstName = input("Type the Customer's first name: ")
  CustLastName = input("Type the Customer's last Name: ")
  CustCity = input("enter customer's city name: ")
  CustPCode = input("Type the customer's Postal Code: ")
  validatePostalCode(CustPCode.upper())
  CustCCard = (input("type the customer's Credit Card: "))
  validateCreditCard(CustCCard)
#lets code know to use variable CustCCard when validating
#define and open file
def validatePostalCode(CustPCode):
  postalCodesFile = open("postal_codes.csv", "r")
  postalCodes = postalCodesFile.read().splitlines()
#check validation, the 3 only checks the first 3 digits
  valid = False
  for code in postalCodes:
      if CustPCode == code[:3]:
          valid = True
          break
  #print
  if valid:
      print("POSTAL CODE ENTERED IS VALID.")
  else:
      print("INVALID POSTAL CODE ENTERED")
  

def validateCreditCard(CustCCard):
    # declare variables
    sumOddDigits = 0
    sumEvenDigits = 0
    total = 0
#removes spaces or hyphens in the code and reverses the number inputted
    CustCCard = CustCCard.replace("-", "")
    CustCCard = CustCCard.replace(" ", "")
    CustCCard = CustCCard[::-1]
#makes sure that the number follows credit card rules
#and makes sure the number is divisible by 10 and adds the total of odd and even numbers
    for x in CustCCard[::2]:
        sumOddDigits += int(x)
    for x in CustCCard[1::2]:
        x = int(x) * 2
        if x >= 10:
            sumEvenDigits += (1 + (x % 10))
        else:
            sumEvenDigits += x
    total = sumOddDigits + sumEvenDigits

    if total % 10 == 0:
        print("CREDIT CARD NUMBER IS VALID.")
    else:
        print("INVALID CREDIT CARD NUMBER ENTERED")

def generateCustomerDataFile():
    folder = os.getcwd()
#get current working directory with a custom file name and an existing folder
    fileName = input("Generating new customer file...\nWhat do you want to name this file? ")
    folderName = input("Which existing folder would you like to assign the file to? ")
    fileCreateNew = folder + folderName + "\\" + fileName + ".txt"
#file is set to nothing to show if the file wasn't edited successfully
    file = ("")
    try:
#file is opened, written on, and closed
        file = open(fileName, "w")
        file.writelines("NEW CUSTOMER PROFILE\n-------------")
        file.writelines("First Name: " + CustFirstName + "\n")
        file.writelines("Last Name: " + CustLastName + "\n")
        file.writelines("City: " + CustCity + "\n")
        file.writelines("Postal Code: " + CustPCode + "\n")
        file.writelines("Credit Card Number: " + CustCCard + "\n")
        print("FILE SAVED IN FOLDER:", folderName)
    finally:
        if file:
            file.close()
        

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################

####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

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

#374245455400126
