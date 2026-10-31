print("=============Welcome to the Interactive Personal Data Collector!=============")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))

print("Thank you! Here is the information we collected:")
print(f"Name: {name} Type: {type(name)}, Memory Address: {id(name)}")
print(f"Age: {age} Type: {type(age)}, Memory Address: {id(age)}")
print(f"Height: {height} meters Type: {type(height)}, Memory Address: {id(height)}")
print(f"Favorite Number: {favourite_number} Type: {type(favourite_number)}, Memory Address: {id(favourite_number)}")

birth_year = 1992 - age
print(f"Your birth year is approximately: {birth_year}(based on your {age})")

print("=============Thank you for using the Personal Data Collector. Goodbye!=============")