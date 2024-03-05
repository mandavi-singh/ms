#problem 3 username validation
try:
    username = str(input("Enter the username: "))
    if len(username) >= 5 and username.isalnum():
        print("valid username.")
    else:
        print("Invalid username.")
except ValueError:
    print("An error occurred.")