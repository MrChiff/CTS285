from M1HW_hardwick_math import Calculations

class UI:
    
    """
    This class coordinates and displays the user interface for the program.
    
    inputs:  none
    outputs:  displays the user interface
    """
    
    #=================#
    def mainMenu(self):
    #=================#
    
        """ 
        This function displays the main menu to the user. 
        
        inputs: none
        outputs: sent (user selection/sentinel value) and displays main menu
        """
        
        while True:
            
            # Ask the user to choose one of the options.
            try:
                sent = int(input("\n-------------- Calculator --------------\n"\
                                   "1) Add\n"\
                                   "2) Subtract\n"\
                                   "3) Divide\n"\
                                   "4) Multiply\n"\
                                   "0) Exit the program.\n"\
                                   "----------------------------------------\n"\
                                   "Enter your choice:\t"))
                    
            # If the user does not enter an int, display an error message.
            except ValueError:
                print("\nPlease input a valid integer value.")
            
            # General error statement.
            except:
                print("General Error.")
            
            # Int input validation. 
            else:
                
                # If the user's input is an integer but not and appropriate choice: 
                if (sent > 4 or sent < 0):
                    UI().errorMessage()
                    UI().mainMenu()
                
                # If the user's input passes the previous validation steps, break the while loop and 
                # return "sent" (the sentinel value).
                else:
                    break
        
        return sent
    
    #=====================#
    def errorMessage(self):
    #=====================#
    
        """ 
        This function lets the user know that the option chosen is not in the menu. 
        
        inputs: none
        outputs: displays error message and the main menu
        """
        
        print("\nError:  Your choice is not valid.  Please enter a corrrect value.")
    
    #=====================#    
    def generalError(self):
    #=====================#
    
        """
        This function lets the user/developer know that a general error has occurred A general error
        is one not explicitly stated by the exception handling.
        
        inputs:  none
        outputs: general error message
        """
    
        print("General Error.")
    
    #===================#    
    def getNumbers(self):
    #===================#
        
        """
        This funtion asks the user to enter the numbers to be used in the calculations 
        (M1HW_hardwick_math.py).
        
        inputs:  none
        outputs:  a tuple with the entered values
        """
        
        try:
            a = float(input("Enter a number:  "))
            b = float(input("Enter a number:  "))
        
        except ValueError:
            UI().errorMessage()
            print("Your input must be a DECIMAL or INTEGER number.")
        
        # General error statement.
        except:
            UI().generalError()
        
        # Int input validation. 
        else: 
        
            return (a,b)
    
    #===============#
    def repeat(self):
    #===============#
    
        """
        This function asks the user if he wants to repeat the same type of calculation or if he 
        wants to return to the main menu.
        
        inputs:  none
        outputs:  cont (continuation variable)
        """
        while True:
            try:
                # Asking the user how he wants to proceed.
                cont = int(input(("1. Repeat\n" \
                                  "2. Main Menu\n" \
                                  "Enter a number: ")))
                
                # If the user does not enter 1 or 2.
                if (cont < 1 or cont > 2):
                    raise ValueError
            
            # If the user does not enter an appropriate int, display an
            # error message.
            except ValueError:
                
                UI().errorMessage()
            
            # Catch-all general error.
            except:
                UI().generalError()
                
            else:
                break
        
        return cont
    
    #======================#
    def option1(self, cont):
    #======================#
    
        """
        This function handles the operations of Option 1: Add.  This functions asks the user to 
        enter the numbers he wants to add (UI().getNumbers()).  Add the numbers together
        (Calculations().add(a,b)). Asks the user if he wants to repeat the calculation with 
        different numbers or return to the main menu (UI().repeat()).
        
        inputs:  cont (initialized continuation variable)
        outputs:  displays the option label and the math opteration.
        """
    
        # While the user wants to continue with the calculation:
        while cont != 2:
            
            # Print option label.
            print("\n |================|"\
                  "\n | OPTION 1:  Add |"\
                  "\n |================|\n")
                
            (a,b) = UI().getNumbers()
            Calculations().add(a,b)
            cont = UI().repeat()
    
    #======================#
    def option2(self, cont):
    #======================#
    
        """
        This function handles the operations of Option 2: Subtract.  This functions asks the user to 
        enter the numbers he wants to subtract (UI().getNumbers()).  Subtract the numbers from each
        other (Calculations().subtract(a,b)). Asks the user if he wants to repeat the calculation 
        with different numbers or return to the main menu (UI().repeat()).
        
        inputs:  cont (initialized continuation variable)
        outputs:  displays the option label and the math opteration.
        """
    
        # While the user wants to continue with the calculation:
        while cont != 2:
            
            # Print option label.
            print("\n |=====================|"\
                  "\n | OPTION 2:  Subtract |"\
                  "\n |=====================|\n")
                
            (a,b) = UI().getNumbers()
            Calculations().subtract(a,b)
            cont = UI().repeat()
    
    #======================#
    def option3(self, cont):
    #======================#
    
        """
        This function handles the operations of Option 3: Multiply.  This functions asks the user to 
        enter the numbers he wants to add (UI().getNumbers()).  Multiply the numbers together
        (Calculations().multiply(a,b)). Asks the user if he wants to repeat the calculation with 
        different numbers or return to the main menu (UI().repeat()).
        
        inputs:  cont (initialized continuation variable)
        outputs:  displays the option label and the math opteration.
        """
    
        # While the user wants to continue with the calculation:
        while cont != 2:
            
            # Print option label.
            print("\n |===================|"\
                  "\n | OPTION 3:  Divide |"\
                  "\n |===================|\n")
                
            (a,b) = UI().getNumbers()
            Calculations().divide(a,b)
            cont = UI().repeat()
        
    #======================#
    def option4(self, cont):
    #======================#
    
        """
        This function handles the operations of Option 4: Divide.  This functions asks the user to 
        enter the numbers he wants to add (UI().getNumbers()).  Divide the numbers 
        (Calculations().divide(a,b)). Asks the user if he wants to repeat the calculation with 
        different numbers or return to the main menu (UI().repeat()).
        
        inputs:  cont (initialized continuation variable)
        outputs:  displays the option label and the math opteration.
        """
    
        # While the user wants to continue with the calculation:
        while cont != 2:
        
            # Print option label.
            print("\n |=====================|"\
                  "\n | OPTION 4:  Multiply |"\
                  "\n |=====================|\n")
                
            (a,b) = UI().getNumbers()
            Calculations().multiply(a,b)
            cont = UI().repeat()