#Checking if the user's input is odd or even.

#User Input
user_input = int(input("What is your number?: "))

#If statements to check is the modulo left over is 0 (even) or 1 (odd).
if user_input % 2 == 0:
    print("Your number is even.")
elif user_input % 2 == 1:
    print("Your number is odd.")
else:
    print("Invalid input.")
