import random

num_dice = int(input("How many dice would you like to roll? "))

total_sum = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)  # Each die can roll between 1 and 6
    total_sum += roll

# Print the total sum of the rolls
print(f"The sum of the rolled dice is: {total_sum}")