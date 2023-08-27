class Calculations:
    
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b
        
        
    # def add(self, a, b):
    #     return a + b
    
    # def add(self):
    #     return self.a + self.b
    
    def add(self, a, b):
        print(a, " + ", b, "=", a+b, "\n")

    def subtract(self, a, b):
        print(a, " - ", b, "=", a-b, "\n")

    def divide(self, a, b):
        try:
            ans = a/b
            
        except ZeroDivisionError:
            print("Division by zero! Please use a different denominator.\n")
            
        else:
            print(a, " \N{DIVISION SIGN} ", b, "=", ans, "\n")

    def multiply(self, a,b):
        print(a, " \N{MULTIPLICATION SIGN} ", b, "=", a*b, "\n")
        
    # def __repr__(self):
        
    #     if self.key is None:
    #         print("Empty")
    #     else:
    #         print("Node: " + str(self.key))
