# CTS 285
# M1HW
# Jonathan Hardwick
# 23/08/30


from M1HW_hardwick_math import Calculations
from M1HW_hardwick_UI import UI

# #=============#
# def mainMenu():
# #=============#

#     """ 
#     This function displays the main menu to the user. 
    
#     inputs: none
#     outputs: sent (user selection/sentinel value) and displays main menu
#     """
    
#     while True:
        
#         # Ask the user to choose one of the options.
#         try:
#             sent = int(input("\n----------------- Menu -----------------\n"\
#                                "1) Add\n"\
#                                "2) Subtract\n"\
#                                "3) Divide\n"\
#                                "4) Multiply\n"\
#                                "0) Exit the program.\n"\
#                                "----------------------------------------\n"\
#                                "Enter your choice:\t"))
                
#         # If the user does not enter an int, display an error message.
#         except ValueError:
#             print("\nPlease input a valid integer value.")
        
#         # General error statement.
#         except:
#             print("General Error.")
        
#         # Int input validation. 
#         else:
            
#             # If the user's input is an integer but not and appropriate choice: 
#             if (sent > 5):
#                 errorMessage()
#                 mainMenu()
            
#             # If the user's input passes the previous validation steps, break the while loop and 
#             # return "sent".
#             else:
#                 break
    
#     return sent

# #=================#
# def errorMessage():
# #=================#

#     """ 
#     This function lets the user know that the option chosen is not in the menu. 
    
#     inputs: none
#     outputs: displays error message and the main menu
#     """
    
#     print("\nError:  Your choice is not valid.  Please enter a corrrect value.")
    
# def calcAdd(a, b):
#     return a + b

# def calcSubtract(a, b):
#     return a-b

# def calcDivide(a, b):
#     return a/b

# def calcMultiply(a,b):
#     return a*b

# def getNumbers():
    
#     a = float(input("Enter a number:  "))
#     b = float(input("Enter a number:  "))
    
#     return (a,b)

# def repeat():
    
#     """
#     This function asks the user if he wants to continue for the option he is currently
#     using at the time.

#     inputs: none
#     outputs: cont (the continuation sentinel value)
#     """
        
#     while True:
#         try:
#             # Asking the user how he wants to proceed.
#             cont = int(input(("1. Repeat\n" \
#                               "2. Main Menu\n" \
#                               "Enter a number: ")))
            
#             # If the user does not enter 1 or 2.
#             if (cont < 1 or cont > 3):
#                 raise ValueError
        
#         # If the user does not enter an appropriate int, display an
#         # error message.
#         except ValueError:
            
#             print("\nPlease input a valid integer value.")
        
#         # Catch-all general error.
#         except:
#             print("\nGeneral Error.")
            
#         else:
#             break
    
#     return cont

# Add number validation/exception handling to getNumbers() 
# should the display of the math equation be put in the calc* functions
# Ask Norris how I should send the numbers to the Calculations class (commented vs uncommented 
#   version of Calculations.add())
# add division by zero exception in option 4: divide
# consider recursion instead of while 


#=========#
def main():
#=========#

    # Initialize the sentinel value to zero.
    sent = -1

    # While the user wants to continue to use the program (the sentinel value is not equal to 0):
    while sent != 0:
    
        # Display the main menu to the user.
        sent = UI().mainMenu()
        
        # Initialize the continuation value.
        cont = -1
        
        #================#
        # OPTION 1:  Add #
        #================#
        
        # If the user chooses option 1:
        if sent == 1:
            
            # While the user wants to continue with the purchase:
            while cont != 2:
                
                cont = UI().option1()
                    
        #=====================#
        # OPTION 2:  Subtract #
        #=====================#
        
        # If the user chooses option 1:
        if sent == 2:
            
            # While the user wants to continue with the purchase:
            while cont != 2:
                
                cont = UI().option2()
             
        #===================#
        # OPTION 3:  Divide #
        #===================#
        
        # If the user chooses option 3:
        elif sent == 3:
            
            while cont != 2:
                
                cont = UI().option3()
                            
        #=====================#
        # OPTION 4:  Multiply #
        #=====================#
        
        # If the user chooses option 4:
        elif sent == 4:
            
            while cont != 2:
                
                cont = UI().option4()      
            
        #==============================#
        # OPTION 5:  Exit the program. #
        #==============================#
        
        # If the user chooses option 5:
        elif sent == 0:
            
            # Display a good-bye message and terminate the program.
            print("\nExiting Program.")

# Call the main function.
if __name__ == "__main__":    
    main()
