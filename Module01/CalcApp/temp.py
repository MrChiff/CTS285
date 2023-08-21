# CTS 285 Calc App


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
                               "1) Purchase an item.\n"\
                               "2) View inventory.\n"\
                               "3) Sell an item.\n"\
                               "4) View total inventory value.\n"\
                               "5) Exit the program.\n"\
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
    
def CalcAdd(a, b):
    return a + b

def CalcSubtract(a, b):
    return a-b

def CalcDivide(a, b):
    return a/b

def CaclMultiply(a,b):
    return a*b

def GetNumbers():
    
    
#=========#
def main():
#=========#

    # Initialize the sentinel value to zero.
    sent = 0

    # While the user wants to continue to use the program (the sentinel value is not equal to 5):
    while sent != 5:
    
        # Display the main menu to the user.
        sent = mainMenu()
        
        #==============================#
        # OPTION 1:  Purchase an item. #
        #==============================#
        
        # If the user chooses option 1:
        if sent == 1:
            
            # Initialize the continuation value. (just for this option)
            cont = 1
            
            # While the user wants to continue with the purchase:
            while cont != 2:
                
                while True:
                    
                    # Print option label.
                    print("\n |================|"\
                          "\n | OPTION 1:  Add |"\
                          "\n |================|\n")
                    
                    
                    # If the user does not want to continue he can type "cancel" to end the 
                    # transaction.
                    if itemName == "cancel":
                        break
                    
                    # Assigns the node with the matching name to a new variable (this makes the 
                    # variable name shorter when referencing it later in the code.
                    purchase = shop_inventory.ListSearch(itemName)
                    
                    # If the item is found in the store's inventory:
                    if purchase:
                        
                        # Initialize item quantity.
                        itemQuantity = -1
                        
        
                        while itemQuantity < 0:
                            try: 
                                # Prompt the user for the number of items he wants to purchase.
                                itemQuantity = int(input("\nHow many " + itemName + "s do you want to buy?\t"))
                                
                                if (itemQuantity < 0):
                                    raise ValueError
                                
                            # If the user does not enter a positive int, display an error message.
                            except ValueError:
                                print("\nPlease use only positive integer values.")
                            
                            # General error statement.
                            except:
                                print("General Error.")
                        
                        
                        # Check to see if the item is in the shop inventory
                        if (itemQuantity <= purchase.quant):
                            
                            print("\n" + itemName.capitalize() + " found in stock! (quantity: " \
                                  + str(purchase.quant) + ")\n")
                            time.sleep(3)
                            
                            # Checking to make sure funds are available.
                            if (player_money < purchase.price*itemQuantity):
                                print("\nYou do not have enough funds to make this purchase.")
                                time.sleep(3)
                                break
                            
                            else:
                                # Updating player currency.
                                player_money = player_money - purchase.price * itemQuantity
                            
                            if TESTING:
                                print()
                                printInventory("player (before purchase)", player_inventory)
                                time.sleep(3)
                            
                            # Does the player already have this item?
                            item_in_player_inventory = player_inventory.ListSearch(itemName)
                            
                            # Updating player inventory.
                            # If the same type of item already exists in the player inventory:
                            if item_in_player_inventory:
                                
                                # Increase the quantity of the item in the player's inventory
                                update_player_node = Node(item_in_player_inventory.item,\
                                                          item_in_player_inventory.price,\
                                                          item_in_player_inventory.quant + itemQuantity)
                                
                                # can update node.quant directly
                                # node.quant = node.quant +/- itemQuantity
                                
                                
                                # Updating player_inventory linked list
                                existingItemQuantityUpdate(player_inventory, item_in_player_inventory,\
                                                           update_player_node)
                                
                            # If the item is not in the player inventory:
                            else:    
                                # Add new item to player's inventory.
                                player_inventory.append(Node(purchase.item, purchase.price, itemQuantity))
                                
                            printInventory("player", player_inventory)
                            print("Amount of gold: ", player_money)
                            time.sleep(3)
                            
                            # Create new shop_inventory node
                            update_shop_node = Node(purchase.item, purchase.price, purchase.quant - itemQuantity)
                            # Update shop_inventory item quantity
                            existingItemQuantityUpdate(shop_inventory, purchase, update_shop_node)
                            
                            if TESTING:
                                print()
                                printInventory("updated shop", shop_inventory)
                                time.sleep(3)
                        
                        # Make sure there are enough items in stock.
                        else:
                            
                            print("\nThere are not " + str(itemQuantity) + " " + itemName + "s in stock. "\
                                  "You can only purchase " + str(purchase.quant) + " or fewer." )
                            time.sleep(3)
                            
                        break
                    
                    # If the item is not found in the shop inventory.
                    else:
                        
                        print("\n" + itemName.capitalize() + " not found! Try again!")
                        time.sleep(3)
                    
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
                    
        #============================#
        # OPTION 2:  View inventory. #
        #============================#
        
        # If the user chooses option 2:
        elif sent == 2:
            
            print("\n |============================|"\
                  "\n | OPTION 2:  View inventory. |"\
                  "\n |============================|\n")
            
            # Display player's inventory.
            printInventory("player", player_inventory)
            
            # Display player's currency
            print("Amount of gold: ", player_money)
             
        #==========================#
        # OPTION 3:  Sell an item. #
        #==========================#
        
        # If the user chooses option 3:
        elif sent == 3:
            
            cont = 1
            while cont != 2:
                
                while True:
                    
                    # Print option label.
                    print("\n |==========================|"\
                          "\n | OPTION 3:  Sell an item. |"\
                          "\n |==========================|\n")
                        
                    # Display the shops inventory to determine what and how much to purchase    
                    printInventory("player", player_inventory)
                    
                    # Remind the user how much money he has to use.
                    print("Amount of gold: ", player_money)
                    
                    # Prompt the user for the name of the item he wants to sell.
                    itemName = input("""\nWhat is the item that you want to sell? ("cancel" to exit)\t""")
                    itemName = itemName.strip().lower()
                    
                    if itemName == "cancel":
                        break
                    
                    # Finding the item the player wants to sell.
                    selling = player_inventory.ListSearch(itemName)
                    
                    if selling:
                        
                        itemQuantity = -1
                    
                        while itemQuantity < 0:
                            try: 
                                # Prompt the user for the number of items he wants to purchase.
                                itemQuantity = int(input("\nHow many " + itemName + "s do you want to sell?\t"))
                                
                                if (itemQuantity < 0):
                                    raise ValueError
                                    
                            # If the user does not enter an int, display an error message.
                            except ValueError:
                                print("\nPlease use only positive integer values.")
                            
                            # General error statement.
                            except:
                                print("General Error.")
                        
                        if TESTING:
                            print("\nYou want to sell " + str(itemQuantity) + " " + itemName + "s.\n")
                        else:
                            print()
                        
                        # If the item is found in the player's inventory and the quantity to sell does
                        # not exceed the inventory quantity:
                        if (itemQuantity <= selling.quant):
                            
                            player_money = player_money + selling.price * itemQuantity
                            
                            if TESTING:
                                printInventory("shop (before sale)", shop_inventory)
                                time.sleep(3)
                                
                            # Does the player already have this item?
                            item_in_shop_inventory = shop_inventory.ListSearch(itemName)
                            
                            # Updating shop inventory.
                            # If the same type of item already exists in the shop's inventory:
                            if item_in_shop_inventory:
                                
                                # Increase the quantity of the item in the shop's inventory
                                update_shop_node = Node(item_in_shop_inventory.item,\
                                                          item_in_shop_inventory.price,\
                                                          item_in_shop_inventory.quant + itemQuantity)
                                    
                                # Updating player_inventory linked list
                                existingItemQuantityUpdate(shop_inventory, item_in_shop_inventory,\
                                                           update_shop_node)
                                    
                            # If the item is not in the shop inventory:
                            else:    
                                # Add new item to shop's inventory.
                                shop_inventory.append(Node(selling.item, selling.price, itemQuantity))
                            
                            if TESTING:
                                printInventory("shop", shop_inventory)
                                time.sleep(3)
                            
                            # Create new player_inventory node
                            update_player_node = Node(selling.item, selling.price,\
                                                      selling.quant - itemQuantity)
                            # Update player_inventory item quantity
                            existingItemQuantityUpdate(player_inventory, selling, update_player_node)
                            
                            if TESTING:
                                printInventory("player", player_inventory)
                                time.sleep(3)
                            
                            print("Amount of gold: ", player_money)
                            break
                        
                        # If the item is found in the player's inventory but the quantity to sell
                        # exceeds the inventory quantity:  display an error
                        else:
                            print("You don't have " + str(itemQuantity) + " " + itemName + \
                                  "s. (quantity cannot exceed inventory)")
                            time.sleep(3)
                                
                    else:
                        
                        print("\n" + itemName.capitalize() + " not found! Try again!")
                        time.sleep(3)
                        
                while True:
                    try:
                        # Asking the player if he wants to purchase another item
                        cont = int(input("\nDo you want to sell another item?\n" + \
                                     "1) Yes\n" + \
                                     "2) No\n"))
                            
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
            
            print("\n |========================================|"\
                  "\n | OPTION 4:  View total inventory value. |"\
                  "\n |========================================|\n")
            
            printInventory("player", player_inventory)
            print("Total Value = ", player_inventory.inventoryValue())
            
            
        #==============================#
        # OPTION 5:  Exit the program. #
        #==============================#
        
        # If the user chooses option 5:
        elif sent == 5:
            
            # Display a good-bye message and terminate the program.
            print("\nExiting Program.")

# Call the main function.
if __name__ == "__main__":    
    main()