
def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return f"The result is: {result}"
    except ZeroDivisionError:
        return "You cannot divide by zero"
    except ValueError:
        return "Invalid input. Please enter numbers only"
