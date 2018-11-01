number = int(input("Enter your number "))
check = int(input("Give me a number to divide by"))

if number % 2 == 0:
    print("Even number")
if number % 4 == 0:
    print("Number is a multiple of 4")
else:
    print("Odd number")

if number%check ==0:
    print(number, "divides evenly by ", check)
else:
    print(number, "does not divide evenly by", check)
