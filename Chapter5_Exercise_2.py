# Initialize an empty list to store the numbers
numbers = []


while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
    if user_input == "":
        break
    
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

numbers.sort(reverse=True)

# Print the top five numbers
print("The five greatest numbers are:")
print(numbers[:5])