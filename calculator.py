class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b  # Fixed the order of subtraction

    def multiply(self, a, b):
        result = 0
        for _ in range(abs(b)):
            result = self.add(result, a)
        return result if b >= 0 else -result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        # Use true division to get a float result
        result = a / b
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot calculate modulo by zero")
        remainder = abs(a)
        while remainder >= abs(b):
            remainder -= abs(b)
        return remainder if a >= 0 else -remainder


# Example usage (optional to test)
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
