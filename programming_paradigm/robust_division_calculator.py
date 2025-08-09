
def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return f"The result is: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Invalid input. Please enter numbers only"
