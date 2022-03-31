class Сalculator():

    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            return "Error: division by zero"
        return x / y

    def raise_to_power(self, x, y):
        return x ** y
