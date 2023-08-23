# CTS 285
# M1HW
# Jonathan Hardwick
# 23/08/30

# Add description!!


#=============#
def mainMenu():
#=============#
  """ 
    This function displays the main menu to the user. 
    
    inputs: none
    outputs: sent (user selection/sentinel value) and displays main menu
    """

  while True:

    # Ask the user to choose one of the options.
    try:
      sent = int(input("\n----------------- Menu -----------------\n"\
                         "1) Add\n"\
                         "2) Subtract\n"\
                         "3) Divide\n"\
                         "4) Multiply\n"\
                         "0) Exit the program.\n"\
                         "----------------------------------------\n"\
                         "Enter your choice:\t"))

    # If the user does not enter an int, display an error message.
    except ValueError:
      print("\nPlease enter an appropriate choice.")

    # General error statement.
    except:
      print("General Error.")

    # Int input validation.
    else:

      # If the user's input is an integer but not and appropriate choice:
      if (sent > 5):
        errorMessage()
        mainMenu()

      # If the user's input passes the previous validation steps, break the while loop and
      # return "sent".
      else:
        break

  return sent


#=================#
def errorMessage():
  #=================#
  """ 
    This function lets the user know that the option chosen is not in the menu. 
    
    inputs: none
    outputs: displays error message and the main menu
    """

  print("\nError:  Your choice is not valid.  Please enter a corrrect value.")


#================#
def calcAdd(a, b):
  #================#
  return a + b


#=====================#
def calcSubtract(a, b):
  #=====================#
  return a - b


#===================#
def calcDivide(a, b):

  return a / b


def caclMultiply(a, b):
  return a * b


#===============#
def getNumbers():
  #===============#

  a = float(input("Enter a number:  "))
  b = float(input("Enter a number:  "))

  return (a, b)


#===========#
def repeat():
  #===========#

  cont = int(input(("1. Repeat\n" \
                    "2. Main Menu\n" \
                    "Enter a number: ")))
  return cont


#=========#
def main():
  #=========#

  # Initialize the sentinel value to zero.
  sent = -1

  # While the user wants to continue to use the program (the sentinel value is not equal to 5):
  while sent != 0:

    # Display the main menu to the user.
    sent = mainMenu()

    #================#
    # OPTION 1:  Add #
    #================#

    # If the user chooses option 1:
    if sent == 1:

      # Initialize the continuation value. (just for this option)
      cont = -1

      # While the user wants to continue with the purchase:
      while cont != 2:

        # Print option label.
        print("\n |================|"\
              "\n | OPTION 1:  Add |"\
              "\n |================|\n")

        a, b = getNumbers()
        print(a, " + ", b, "=", calcAdd(a, b), "\n")

        while True:
          try:
            # Asking the player if he wants to purchase another item.
            cont = int(input("\nDo you want to sell another item?\n" + \
                         "1) Yes\n" + \
                         "2) No\n"))

            # If the user does not enter 1 or 2.
            if (cont < 0 or cont > 3):
              raise ValueError

          # If the user does not enter an int, display an error message.
          except ValueError:

            print("\nPlease input a valid integer value.")

          # Catch-all general error.
          except:
            print("\nGeneral Error.")

          else:
            break

    #=====================#
    # OPTION 2:  Subtract #
    #=====================#

    # If the user chooses option 1:
    if sent == 2:

      # Initialize the continuation value. (just for this option)
      cont = -1

      # While the user wants to continue with the purchase:
      while cont != 2:

        # Print option label.
        print("\n |=====================|"\
              "\n | OPTION 2:  Subtract |"\
              "\n |=====================|\n")

        a, b = getNumbers()
        print(a, " - ", b, "=", calcSubtract(a, b), "\n")

        while True:
          try:
            # Asking the player if he wants to purchase another item.
            cont = repeat()

            # If the user does not enter 1 or 2.
            if (cont < 0 or cont > 3):
              raise ValueError

          # If the user does not enter an int, display an error message.
          except ValueError:

            print("\nPlease input a valid integer value.")

          # Catch-all general error.
          except:
            print("\nGeneral Error.")

          else:
            break

    #==========================#
    # OPTION 3:  Sell an item. #
    #==========================#

    # If the user chooses option 3:
    elif sent == 3:

      cont = 1
      while cont != 2:

        while True:

          # Print option label.
          print("\n |===================|"\
                "\n | OPTION 3:  Divide |"\
                "\n |===================|\n")

          a, b = getNumbers()
          print(a, " / ", b, "=", calcDivide(a, b), "\n")

        while True:
          try:
            # Asking the player if he wants to purchase another item
            cont = repeat()

            if (cont < 0 or cont > 3):
              raise ValueError

          # If the user does not enter an int, display an error message.
          except ValueError:

            print("\nPlease input a valid integer value.")

          # Catch-all general error.
          except:
            print("\nGeneral Error.")

          else:
            break

    #========================================#
    # OPTION 4:  View total inventory value. #
    #========================================#

    # If the user chooses option 4:
    elif sent == 4:

      print("\n |=====================|"\
            "\n | OPTION 4:  Multiply |"\
            "\n |=====================|\n")

      a, b = getNumbers()
      print(a, " x ", b, "=", calcMultiply(a, b), "\n")

      # while True:
      #        try:
      #            # Asking the player if he wants to purchase another item
      #            cont = repeat()

      #            if (cont < 0 or cont > 3):
      #                raise ValueError

      #        # If the user does not enter an int, display an error message.
      #        except ValueError:

      #            print("\nPlease input a valid integer value.")

      #        # Catch-all general error.
      #        except:
      #            print("\nGeneral Error.")

      #        else:
      #            break

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
