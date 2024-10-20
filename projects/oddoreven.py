#Checking if the user's input is odd or even.

#User Input
user_input = int(input("What is your number?: "))

#If statement to check is the modulo left over is 0 (even).
if user_input % 2 == 0:
    print("Your number is even.")
#If module != 0, prints odd.
else:
    print("Your number is odd.")
