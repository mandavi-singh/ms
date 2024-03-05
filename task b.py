 #problem 2 temperature converter
try:
    temperature = float(input("Enter the temperature: "))
    unit = input("Enter the unit(C or F): ")
    if unit == "C":
        converted_temp = (temperature * 9/5) + 32
        print("The temperature in farenheit: ",converted_temp)
    elif unit == "F":
        converted_temp = (temperature - 32) * 5/9
        print("The temperature in celcius: ",converted_temp)
    else:
        print("Invalid unit")
except ValueError:
    print("Invalid input")

