#problem 4 compare string length
try:
    string1 = str(input("Enter the first string: "))
    string2 = str(input("Enter the second string: "))
    if len(string1) > len(string2):
        print("The first string is longer.")
    elif len(string1) < len(string2):
        print("The second string is longer.")
    else:
        print("Both strings are equal length.")
except ValueError:
    print("Invalid input.")
