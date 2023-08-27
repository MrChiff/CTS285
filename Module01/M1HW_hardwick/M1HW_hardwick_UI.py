from M1HW_hardwick_math import Calculations

class UI:
    
    # from M1HW_hardwick_math import Calculations
    
    #=============#
    def mainMenu(self):
    #=============#
    
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
                if (sent > 4):
                    UI().errorMessage()
                    UI().mainMenu()
                
                # If the user's input passes the previous validation steps, break the while loop and 
                # return "sent".
                else:
                    break
        
        return sent
    
    #=================#
    def errorMessage(self):
    #=================#
    
        """ 
        This function lets the user know that the option chosen is not in the menu. 
        
        inputs: none
        outputs: displays error message and the main menu
        """
        
        print("\nError:  Your choice is not valid.  Please enter a corrrect value.")
    
    #===============#    
    def getNumbers(self):
    #===============#
        
        a = float(input("Enter a number:  "))
        b = float(input("Enter a number:  "))
        
        return (a,b)
    
    #===============#
    def repeat(self):
    #===============#
            
        while True:
            try:
                # Asking the user how he wants to proceed.
                cont = int(input(("1. Repeat\n" \
                                  "2. Main Menu\n" \
                                  "Enter a number: ")))
                
                # If the user does not enter 1 or 2.
                if (cont < 1 or cont > 3):
                    raise ValueError
            
            # If the user does not enter an appropriate int, display an
            # error message.
            except ValueError:
                
                print("\nPlease input a valid integer value.")
            
            # Catch-all general error.
            except:
                print("\nGeneral Error.")
                
            else:
                break
        
        return cont
    
    #================#
    def option1(self):
    #================#
        
        # Print option label.
        print("\n |================|"\
              "\n | OPTION 1:  Add |"\
              "\n |================|\n")
            
        a,b = UI().getNumbers()
        Calculations().add(a,b)
        return UI().repeat()
    
    #================#
    def option2(self):
    #================#
    
        # Print option label.
        print("\n |=====================|"\
              "\n | OPTION 2:  Subtract |"\
              "\n |=====================|\n")
            
        a,b = UI().getNumbers()
        Calculations().subtract(a,b)
        return UI().repeat()
    
    #================#
    def option3(self):
    #================#
    
        # Print option label.
        print("\n |===================|"\
              "\n | OPTION 3:  Divide |"\
              "\n |===================|\n")
            
        a,b = UI().getNumbers()
        Calculations().divide(a,b)
        return UI().repeat()
        
    #================#
    def option4(self):
    #================#
    
        # Print option label.
        print("\n |=====================|"\
              "\n | OPTION 4:  Multiply |"\
              "\n |=====================|\n")
            
        a,b = UI().getNumbers()
        Calculations().multiply(a,b)
        return UI().repeat()