class Calculator:
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
class calculation_type:
    def __init__(self, Arithmetic_Operations):
        self.Arithmetic_Operations =  Arithmetic_Operations
        pass