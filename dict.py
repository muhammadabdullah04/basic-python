country_population = {
    "China": 143,
    "India": 136,
    "USA": 32,
    "Pakistan": 21
}

print(country_population)



# Task 2
user_input = input("Enter a command (print/add/exit): ").lower()

if user_input == "print":
    for country, population in country_population.items():
        print(f"{country}==>{population}")
elif user_input == "add":
    new_country = input("Enter country name: ").lower()
    new_population = int(input("Enter population in crores: "))
    country_population[new_country] = new_population
    print(f"{new_country} added successfully!")
elif user_input == "exit":
    print("Exiting the program.")
else:
    print("Invalid input. Please enter print, add, or exit.")

