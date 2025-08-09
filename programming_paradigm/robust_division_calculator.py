

def safe_divide(numerator, denominator):
    try:
        numerator = int(input("Enter the Numarator:"))
        denominator = int(input("Enter the Denominator:"))
        result = numerator / denominator
        
    except ZeroDivisionError as error:
        print(error)
    except ValueError as NumbersOnly:
        print(NumbersOnly)
    finally:
        if 'result' in locals():
            print(result)
        else:
            print("Enter a valid number")
            
            
safe_divide(numerator='', denominator='')
    
    