# Take user input for name, age and year of their last birthday
name = input("What is your name? ")
age = int(input("How old are you? "))
last_birthday_year = int(input("What year was your last birthday? "))

# Calculate the year the user was born in
birth_year = last_birthday_year - age

# Print a sentence stating the user's name and age
print(f"{name} is {age} years old.")

# Print the year the user was born in
print(f"You were born in {birth_year}.")

# Take user input for two integers and a decimal
x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))
z = float(input("Enter a decimal for z: "))

# Calculate the product of the two integers
product1 = x * y

# Calculate the product of all three numbers
product2 = x * y * z

# Calculate the remainder of each number divided by 2
remainder1 = x % 2
remainder2 = y % 2
remainder3 = z % 2

# Print the product of the two integers
print("The product of x and y is ", product1)

# Print the product of all three numbers
print("The product of x, y, and z is ", product2)

# Print the remainder of each number divided by 2
print(x, " mod ", 2, " is ", remainder1)
print(y, " mod ", 2, " is ", remainder2)
print(z, " mod ", 2, " is ", remainder3)

# Take user input for the numerator and denominator of a fraction
numerator = int(input("Enter the numerator of a fraction: "))
denominator = int(input("Enter the denominator of a fraction: "))

# Calculate the decimal value of the fraction
decimal = numerator / denominator

# Print the decimal value of the fraction
print("The decimal value of the fraction ", numerator, "/", denominator, " = ", decimal)
