# CTS 285
# M1HW
# Jonathan Hardwick
# 23/08/30

# =================================================================================================
# M1HW
# Unless otherwise instructed, you will be paired with a programming partner for this assignment.  
# You do not *have* to write code together, but you are strongly encouraged to. You *do* need to 
# collaborate on coming up with the overall design of the program.
# 
# This exercise tests your ability to turn English requirements into a working program. For this 
# assignment, you will create a simple calculator. You are welcome to use any language you're 
# currently studying. 
# 
# The program should use a simple text menu and text input. You only need to work with integers.
# 
# The program should display a text menu allowing the user to choose a calculation type. After 
# doing this, the user will be prompted to enter two numbers. The program will display the result, 
# then return to the main menu.
# 
# Tier Grading
# We will use a Bronze/Silver/Gold tier system, where Bronze gives a maximum of 80 points, SIlver, 
# a maximum of 90, and Gold up to 100. I recommend you always complete one tier before adding the 
# functionality for later tiers.
# 
# Bronze (80/100)
# The program should allow the user to add or subtract two numbers.
# The program should also allow the user to divide or multiply two numbers.
# 
# Silver (90/100)
# For this tier, the program should work in a way that roughly matches the behavior displayed in 
# the sample output below. You may have to make some assumptions.
# In addition, the program should be written in such a way that a given function either handles 
# user input/output, OR does calculations. (No one function can do both).
# (In other words, your UI code should call special functions to do the calculations.)
# 
# Gold (100/100)
# For this tier, the program should be written in such a way that a given class or module either 
# handles user input/output, OR does calculations.
# In other words, similar to the Silver requirements, but broken into two or more classes or 
# modules.
# 
# Sample Output
# 
# Welcome to the calculator program.
# 1. Add
# 2. Subtract
# 3. Divide 
# 4. Multiply
# 5. Exit
# Enter a number: 1
# 
# Add 
# Enter a number: 2
# Enter a number: 2
# 2 + 2 = 4
# 1. Repeat
# 2. Main Menu
# Enter a number: 1
# 
# Add
# Enter a number: 1
# Enter a number: 1
# 1 + 1 = 2 
# 1. Repeat
# 2. Main Menu
# Enter a number: 1
# Welcome to the calculator program.
# 1. Add
# 2. Subtract
# 3. Divide
# 4. Multiply
# 5. Exit
# Enter a number: 5
# Goodbye.
# =================================================================================================


# =================================================================================================
# "User Storeies"
# As a student I want to use mathematical operations so that I can calculate values.
# =================================================================================================

# Importing necessary libraries.
from M1HW_hardwick_UI import UI

# consider recursion instead of while loop


#=========#
def main():
#=========#

    # Initialize the sentinel value to zero.
    sent = -1

    # While the user wants to continue to use the program (the sentinel value is not equal to 0):
    while sent != 0:
    
        # Display the main menu to the user.
        sent = UI().mainMenu()
        
        #================#
        # OPTION 1:  Add #
        #================#
        
        # If the user chooses option 1:
        if sent == 1:
            
            # Calls the option1 function and sends the initialized cont variable value of -1.
            UI().option1(-1)
                    
        #=====================#
        # OPTION 2:  Subtract #
        #=====================#
        
        # If the user chooses option 1:
        if sent == 2:
            
            # Calls the option2 function and sends the initialized cont variable value of -1.
            UI().option2(-1)
             
        #===================#
        # OPTION 3:  Divide #
        #===================#
        
        # If the user chooses option 3:
        elif sent == 3:
            
            # Calls the option3 function and sends the initialized cont variable value of -1.
            UI().option3(-1)
                            
        #=====================#
        # OPTION 4:  Multiply #
        #=====================#
        
        # If the user chooses option 4:
        elif sent == 4:
            
            # Calls the option4 function and sends the initialized cont variable value of -1.
            UI().option4(-1)      
            
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
