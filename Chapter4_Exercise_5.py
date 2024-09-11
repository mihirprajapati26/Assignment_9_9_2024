# Set the correct username and password
correct_username = "Mihir"
correct_password = "Mihir1234"

# Initialize the attempt counter
attempts = 0

while attempts < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Incorrect username or password.")
        attempts += 1

# Check if the maximum number of attempts has been reached
if attempts == 5:
    print("Access denied.")