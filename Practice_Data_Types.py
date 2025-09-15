# Practice 1
# Celcius = float(input("What is the current temperature in Celcius?: "))
# Fahrenheit = (Celcius * 9/5) + 32
# print("The Temperature in Fahrenheit is " + format(Fahrenheit, ".2f"))

# Practice 2
# First_Name = input("What is Your First Name?: ")
# Last_Name = input("What is Your Last Name?: ")
# Full_Name = (First_Name + " " + Last_Name)
# print(Full_Name.upper())
# print(Full_Name.lower())
# print(Full_Name.title())

# Practice 3
# try:
#     age = int(input("What is your age?: "))
#     if age >= 18:
#         print('you can vote')
#     else:
#         print('you cannot vote')
# except ValueError:
#     print('invalid age input, please input a whole number')

password = input('What is your password?: ')
has_upper = any(ch.isupper() for ch in password)
has_number = any(ch.isdigit() for ch in password)
if has_upper and has_number:
    print('password is strong')
elif has_upper and not has_number:
    print('You have an uppercase but not a number character in your password')
elif has_number and not has_upper:
    print('You have a number but not an uppercase character in your password')
else:
    print('Strong Password must have at least one uppercase character and at least one number character')
