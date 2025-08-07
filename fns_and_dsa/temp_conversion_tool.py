# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature and unit
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            # Convert Fahrenheit to Celsius
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature}°C")
        elif unit == "C":
            # Convert Celsius to Fahrenheit
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature}°F")
        else:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


