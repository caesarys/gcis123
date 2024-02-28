"""
Students: Meera Alshara, Syed Iftesam, Caesar Al Shdaifat
contribution of Syed: Main function (40%)
contribution of Caesar: Docstrings and TroubleShooting(30%)
contribution of Meera: Constants and functions (30%)
Description: This program has been designed to help the user in currency conversion from AED to other major currencies and also allows 
             for it to convert from the other major currencies to AED. The option to exit is also available if the user does not want 
             to convert any of the currencies. 

Repository Links:
Syed : https://github.com/LagSpikeee/GCIS-123/blob/main/group8-activity2.py
Meera : https://github.com/meeralshara/gcis123/blob/main/group8-activity2.py
Caesar : https://github.com/caesarys/gcis123/blob/main/group8-activity2.py
"""

"""
The below values are the constants that have been globally declared that will be used in functions which will aid in currency to currency
conversions.
"""
AED1 = 0.25  # to Euro
AED2 = 0.22  # to British pound
AED3 = 0.27  # to US dollar
EURO = 3.98  # to AED
BRITISHPOUND = 4.65  # to AED
USDOLLAR = 3.67  # to AED

"""
Each individual function below is responsible for certain currency conversion using the constants that were globally declared.
Based on the value the user wants, we muliply the value (money) that the user inputs with the right constant that will ultimately give the result 
of conversion of thier choice.
"""
def aed_to_euro(money):
    conveuro = money * AED1
    return conveuro

def aed_to_britishPound(money):
    convertbrit = money * AED2
    return convertbrit

def aed_to_dollar(money):
    convdollar = money * AED3
    return convdollar

def euro_to_aed(amount):
    converttoaed = amount * EURO
    return converttoaed

def britishPound_to_aed(amount):
    convbrittoaed = amount * BRITISHPOUND
    return convbrittoaed

def dollar_to_aed(amount):
    convdolltoaed = amount * USDOLLAR
    return convdolltoaed

def main():

    while True:  #while True allows this block of command to run indefinately

        """ The print will creates a user interface that gives clear indications for the options available for the user to choose between. """

        print("    \"Main Menu\"    ")
        print("Welcome to currency converter")
        print("------------------------------")
        print("1. AED to other currency \n2. Other currency to AED\n3. Exit")

        """ This will take the value that will be used to further provoke the progrom to move forward and execute. 
            Option 1 will allow AED to other currency convertion
            Option 2 will allow other currency to AED
            Option 3 will exit the program."""

        x = input("Select the conversion direction: ")
        print()

        if x == '1': #This will be executed when '1' is inputed.
            print("1. AED to Euro (EUR)\n2. AED to British Pound (GBP)\n3. AED to US Dollar\n4. Exit")
            b = input("Enter choice: ")
            # If the user chooses option 1, this will be responsible for the conversion from AED to Euro
            if b == '1':
                money = float(input("Enter the amount for conversion: "))
                currency =  aed_to_euro(money)
                print(money, "AED is equal to", currency, "EUR" )
            # If the user chooses option 2, this will be responsible for the conversion from AED to British Pounds
            elif b == '2':
                money = float(input("Enter the amount for conversion: "))
                currency = aed_to_britishPound(money)
                print( money, "AED is equal to", currency, "GBR")   
            # If the user chooses option 3, this will be responsible for the conversion from AED to US Dollars 
            elif b == '3':
                money = float(input("Enter the amount for conversion: "))
                currency =  aed_to_dollar(money)
                print(money, "AED is equal to", currency, "USD")
            # If the user wants to exit the progeam they can put in this option
            elif b == '4':
                print("You have exited the conversion")
                break
            # Incase any other input is entered other than the given option, it will print Invalid Choice and close the program
            else:
                print("Invalid choice")
            
        # If the user wanted to convert from the other currency to AED then they would have inputed this option.           
        elif x == '2':
            print("1. Euro (EUR) to AED\n2. British Pound (GBP) to AED\n3. US Dollar to AED\n4. Exit")
            # The input in this prompt will decide which route of conversion to take
            c = input("Enter choice: ") 
            # This is the first option where Euro is being converted to AED
            if c == '1':
                amount = float(input("Enter the amount for conversion: "))
                currency = euro_to_aed(amount)
                print(amount, "EUR is equal to", currency, "AED")
            # This is the second option where British Pounds are being converted to AED
            elif c == '2':
                amount = float(input("Enter the amount for conversion: "))
                currency = britishPound_to_aed(amount)
                print(amount, "GDB is equal to", currency, "AED")
            # This is the third option where US Dollars are being converted to AED
            elif c == '3':
                amount = float(input("Enter the amount for conversion: "))
                currency = dollar_to_aed(amount)
                print(amount, "USD is equal to", currency, "AED")
            # This gives an option to the user to exit if they do not want to convert anything
            elif c == '4':
                return "You have exited the conversion"
            # This is responsible for exiting if any input other than the given options are entered
            else:
                return "Invalid choice"
        # Out of the first 3 options given, if the user does not want to use the converter they can simply exit with this option
        elif x == '3':
            print("You have exited the conversion")
            break
        # An error will be shown if anything other than the given option are entered
        else:
            print("Invalid choice")
        # This loop is responsible for being persistent and giving a prompt asking if the user wants to continue converting or exit
        while True:
                choice = input("Do you want to continue converting? (y/n): ")
                if choice == 'y':
                    break
                elif choice == 'n':
                    print("Program is exiting")
                    return
                else:
                    print("Please choose either 'y' or 'n' to continue.")

if __name__ == "__main__":
    main()
