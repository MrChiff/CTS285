# CTS 285
# M1HW
# Jonathan Hardwick
# 23/08/30

class Calculations:
    
    """
    This class contains the mathematical operations available is this program.
    
    inputs:  none
    outputs:  displays math operations and answers
    """
    
    # constructorless __init__
    def __init__(self):
        pass
        
    #==================#
    def add(self, a, b):
    #==================#
        
        """
        This function performs the addition math operation.
        
        inputs:  a, b 
        outputs:  displays the addition operation and the answer.
        """
        
        print(a, " + ", b, "=", a+b, "\n")
    
    #=======================#
    def subtract(self, a, b):
    #=======================#
    
        """
        This function performs the subtraction math operation.
        
        inputs:  a, b 
        outputs:  displays the subtraction operation and the answer.
        """
    
        print(a, " - ", b, "=", a-b, "\n")

    #=====================#
    def divide(self, a, b):
    #=====================#
    
        """
        This function performs the division math operation.
        
        inputs:  a, b 
        outputs:  displays the division operation and the answer.
        """
    
        try:
            ans = a/b
            
        except ZeroDivisionError:
            print("Division by zero! Please use a different denominator.\n")
            
        else:
            print(a, " \N{DIVISION SIGN} ", b, "=", ans, "\n")
    
    #=======================#
    def multiply(self, a, b):
    #=======================#
    
        """
        This function performs the multiplication math operation.
        
        inputs:  a, b 
        outputs:  displays the multiplication operation and the answer.
        """
        
        print(a, " \N{MULTIPLICATION SIGN} ", b, "=", a*b, "\n")
