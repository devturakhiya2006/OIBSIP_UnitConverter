# Unit Converter Application

def convert_length():
    print("\nLength Converter")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Feet to Inches")
    print("4. Inches to Feet")
    choice = input("Choose conversion: ")
    value = float(input("Enter value: "))
    
    if choice == '1':
        print(f"{value} meters = {value/1000} kilometers")
    elif choice == '2':
        print(f"{value} kilometers = {value*1000} meters")
    elif choice == '3':
        print(f"{value} feet = {value*12} inches")
    elif choice == '4':
        print(f"{value} inches = {value/12} feet")
    else:
        print("Invalid choice")

def convert_weight():
    print("\nWeight Converter")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    print("3. Pounds to Kilograms")
    print("4. Kilograms to Pounds")
    choice = input("Choose conversion: ")
    value = float(input("Enter value: "))
    
    if choice == '1':
        print(f"{value} kg = {value*1000} grams")
    elif choice == '2':
        print(f"{value} grams = {value/1000} kg")
    elif choice == '3':
        print(f"{value} pounds = {value*0.453592} kg")
    elif choice == '4':
        print(f"{value} kg = {value/0.453592} pounds")
    else:
        print("Invalid choice")

def convert_temperature():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose conversion: ")
    value = float(input("Enter value: "))
    
    if choice == '1':
        print(f"{value}°C = {(value*9/5)+32}°F")
    elif choice == '2':
        print(f"{value}°F = {(value-32)*5/9}°C")
    else:
        print("Invalid choice")

def main():
    while True:
        print("\n=== Unit Converter App ===")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        choice = input("Choose conversion type: ")
        
        if choice == '1':
            convert_length()
        elif choice == '2':
            convert_weight()
        elif choice == '3':
            convert_temperature()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
