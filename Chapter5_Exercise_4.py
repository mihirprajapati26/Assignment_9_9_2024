# Initialize an empty list to store city names
cities = []

for i in range(5):
    city = input(f"Enter the name of city {i + 1}: ")
    cities.append(city)

# Print each city name, one per line
print("The cities you entered are:")
for city in cities:
    print(city)